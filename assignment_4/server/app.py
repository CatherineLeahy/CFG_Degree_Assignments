from flask import Flask, jsonify, request
from db_utils import get_chamber_specs, get_chamber_schedule
from db_utils import schedule_new_project
from datetime import date, timedelta

app = Flask(__name__)


# GET endpoint for getting chamber specification based on ID
@app.route('/chamber/<id>')
def get_chamber_specification(id):
    chamber_specs = get_chamber_specs()
    for chamber_specification in chamber_specs:
        if chamber_specification['id'] == id:
            return jsonify(chamber_specification)
    return jsonify({})


# GET endpoint for getting schedules for a chamber based on ID
@app.route('/chamber/<id>/schedule')
def get_chamber_schedules(id):
    chamber_schedules = get_chamber_schedule(id)
    return jsonify(chamber_schedules)


# GET endpoint for calculating next available slot to run project based on inputted environment and duration
@app.route('/chamber/available')
def get_available_chambers():
    json = request.get_json()
    required_environment = json['environment']
    required_duration = json['duration']
    chamber_specs = get_chamber_specs()
    correct_environ = []

    # filter chambers by correct inputted environment
    for chamber in chamber_specs:
        environment = chamber['environment']
        if environment == required_environment:
            correct_environ.append(chamber['chamber_id'])

    today = date.today()
    available_chamber_start_dates = {}

    # loop through all chambers with correct environments to find the next available slot
    for chamber_id in correct_environ:
        # get schedules for the chamber
        avail_schedules = get_chamber_schedule(chamber_id)

        # if there are no projects in the schedule for the chamber, today's date is used
        if len(avail_schedules) == 0:
            available_chamber_start_dates[chamber_id] = today.strftime("%Y-%m-%d")

        # sort schedules in chronological order by start_date to loop through and check for availability between adjacent projects
        sorted_schedules = sorted(avail_schedules, key=lambda d: d['start_date'])
        print(sorted_schedules)
        days_from_now_to_first = sorted_schedules[0]['start_date'] - today

        # if time between todays date and start date of the first project in the schedule, todays date is used
        if days_from_now_to_first.days > required_duration:
            available_chamber_start_dates[chamber_id]=today.strftime("%Y-%m-%d")
        else:
            # if there is only one project in the schedule then next available slot is the end date of that project
            if len(sorted_schedules) == 1:
                first_schedule_end_date = sorted_schedules[0]['start_date'] + timedelta(days=sorted_schedules[0]['duration'])
                available_chamber_start_dates[chamber_id] = first_schedule_end_date.strftime("%Y-%m-%d")
            else:
                # if there is more than one project in schedule, loop through and compare time between projects to input duration
                for x in range(len(sorted_schedules)-1):
                    current_schedule = sorted_schedules[x]
                    next_schedule = sorted_schedules[x+1]
                    current_schedule_end_date = current_schedule['start_date'] + timedelta(days=current_schedule['duration'])
                    days_from_current_to_next = next_schedule['start_date'] - current_schedule_end_date

                    # if time between the two projects currently being processed is enough to run new project (greater than duration) the end date of the project being processed is used.
                    if days_from_current_to_next.days > required_duration:
                        available_chamber_start_dates[chamber_id]=current_schedule_end_date.strftime("%Y-%m-%d")

                    # if after processing all schedules and no availability is found, use the end date of the last project scheduled
                    elif x+1 == len(sorted_schedules)-1:
                        last_schedule_end_date = next_schedule['start_date'] + timedelta(days=next_schedule['duration'])
                        available_chamber_start_dates[chamber_id]=last_schedule_end_date.strftime("%Y-%m-%d")

    return jsonify(available_chamber_start_dates)


# GET endpoint to get all chamber specs
@app.route('/chamber')
def get_chamber_specifications():
    chamber_specs = get_chamber_specs()
    return jsonify(chamber_specs)


# POST endpoint to add a new project to the schedule based on request body data
@app.route('/new_project', methods=['POST'])
def add_project():
    json = request.get_json()
    print(json)
    new_project = schedule_new_project(json['project_name'], json['start_date'], json['duration'], json['chamber_id'])
    return jsonify(new_project)


if __name__ == '__main__':
    app.run(debug=True, port=5000)