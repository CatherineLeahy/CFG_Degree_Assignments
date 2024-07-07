import requests


# get a chamber spec based on ID
def get_chamber_specification(id):
    result = requests.get(
        'http://127.0.0.1:5000/chamber/{}'.format(id),
        headers={'content-type': 'application/json'}
    )
    return result.json()


# formats and prints a list of chamber specs
def display_chamber_specs(chamber_specification):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15}".format(
        'ID', 'Environment', 'Calibration Due Date'))
    print('-' * 75)

    # print each data item.
    for item in chamber_specification:
        print("{:<15} {:<15} {:<15}".format(
            item['chamber_id'], item['environment'], item['calibration_due_date'][:16]
        ))


# main run function
def run():
    print('#########################################################')
    print('Hello, welcome to the Corrosion Lab scheduling assistant!')
    print('#########################################################')

    while True:
        print()
        option = input('Would you like to:\n1-View all chamber specifications? \n2-View the schedule of a specific chamber? \n3-Add a new project to the schedule?\n4-Exit\nPlease enter option 1, 2, 3 or 4: ')
        if option == '1':
            _view_all_specs()
        elif option == '2':
            _view_specific_schedule()
        elif option == '3':
            _new_project()
        elif option == '4':
            print('Thank you for using the Corrosion Lab scheduling assistant - see you next time!')
            exit()
        else:
            print("Option not recognised. Please try again")


# option to view a schedule for a specific chamber
def _view_specific_schedule():
    input_specific_chamber = input("Please enter the chamber_id for the schedule you want to view: ")
    result = requests.get(
        'http://127.0.0.1:5000/chamber/{}/schedule'.format(input_specific_chamber),
        headers={'content-type': 'application/json'}
    )
    if result.status_code == 200:
        display_chamber_schedules(result.json(), input_specific_chamber)
    else:
        print("Something went wrong, unfortunately we couldn't display the chamber schedule. Please try again.")


# format and print list of chamber schedules
def display_chamber_schedules(chamber_schedule, input_specific_chamber):
    # Print the names of the columns.
    print("##### Schedule Table: {} chamber #####".format(input_specific_chamber))
    print()
    print("{:<20} {:<20} {:<20}".format(
        'Project Name', 'Start Date', 'Duration (days)'))
    print('-' * 75)

    # print each data item.
    for item in chamber_schedule:
        print("{:<20} {:<20} {:<20}".format(
            item['project_name'], item['start_date'][:16], item['duration']
        ))


# format and print dictionary of chamber availability
def display_chamber_availability(chamber_availability):
    print("##### AVAILABLE CHAMBERS #####")
    print()
    print("{:<20} {:<20}".format(
        'Chamber ID', 'Availability Date'))
    print('-' * 75)

    for chamber_id, availability_date in chamber_availability.items():
        print("{:<20} {:<20}".format(
            chamber_id, availability_date
        ))


# option to view all chamber specifications
def _view_all_specs():
    result = requests.get(
        'http://127.0.0.1:5000/chamber',
        headers={'content-type': 'application/json'}
    )
    display_chamber_specs(result.json())


# option to find availability for a new project and then add project to the schedule
def _new_project():
    # get user inputs required for finding chamber availability and validate
    input_environment = input("Which environment do you require? (enter 'acidic' or 'neutral'): ")
    if input_environment != 'acidic' and input_environment != 'neutral':
        print("Invalid environment entered. Please try again")
        return
    input_duration = input('What is the test duration in days (enter a positive integer): ')
    try:
        if int(input_duration) <= 0:
            print("Invalid duration entered. Please try again")
            return
    except ValueError:
        print("Invalid duration entered. Please try again")
        return
    print()

    input_data = {'environment': input_environment, 'duration': int(input_duration)}

    # send a request to GET chamber availability endpoint
    result = requests.get(
        'http://127.0.0.1:5000/chamber/available',
        headers={'content-type': 'application/json'},
        json=input_data
    )
    avail_chambers = (result.json())
    display_chamber_availability(avail_chambers)
    print()

    # get further user inputs required to add a new project to the schedule and validate
    input_chamber_id = input('Please enter the chamber_id of your chosen chamber: ')
    if input_chamber_id not in avail_chambers.keys():
        print("Invalid chamber_id entered. Please try again")
        return
    input_project_name = input('What is the name of your project: ')
    if len(input_project_name) <= 0:
        print("Project name must not be empty. Please try again")
        return

    # structuring request data
    input_data = {'start_date': avail_chambers[input_chamber_id], 'duration': input_duration, 'chamber_id': input_chamber_id, 'project_name': input_project_name}

    # send a request to create a new project
    result = requests.post(
        'http://127.0.0.1:5000/new_project',
        headers={'content-type': 'application/json'},
        json=input_data
    )
    if result.status_code == 200:
        print("Your project has been successfully added to the schedule!")
    else:
        print("Something went wrong, unfortunately we couldn't add your project to the schedule. Please try again.")



if __name__ == '__main__':
    run()

