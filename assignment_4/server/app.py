from flask import Flask, jsonify, request
from db_utils import get_chamber_specs
from db_utils import get_chamber_availability

app = Flask(__name__)


@app.route('/chamber/<id>')
def get_chamber_specification(id):
    chamber_specs = get_chamber_specs()
    for chamber_specification in chamber_specs:
        if chamber_specification['id'] == id:
            return jsonify(chamber_specification)
    return jsonify({})

# @app.route('/chamber/<id>')
# def get_chamber_info(id):
#     chamber_infos = get_chamber_infos()
#     for chamber_info in chamber_infos:
#         if chamber_info['id'] == id:
#             return jsonify(chamber_info)
#     return jsonify({})


@app.route('/availability', methods=['GET'])
def get_availability():
    sample_quantity = input("How many samples you would like to test in the chamber? ").strip()
    duration = input("What is the test duration in days? ")
    environment = input("Do you require an acidic or neutral environment? ")

    available_chambers = get_chamber_availability(sample_quantity,duration,environment)
    return jsonify({})


if __name__ == '__main__':
    app.run(debug=True, port=5000)