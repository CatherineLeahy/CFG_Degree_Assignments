import requests


def get_chamber_specification(id):
    result = requests.get(
        'http://127.0.0.1:5000/chamber/{}'.format(id),
        headers={'content-type': 'application/json'}
    )
    return result.json()


def display_chamber_specs(chamber_specification):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15} {:<15}".format(
        'ID', 'Capacity', 'Environment', 'Calibration Due Date'))
    print('-' * 75)

    # print each data item.
    for item in chamber_specification:
        print("{:<15} {:<15} {:<15} {:<15}".format(
            item['id'], item['capacity'], item['environment'], item['calibration_due_date'][:16]
        ))


def run():
    print('############################')
    print('Hello, welcome to the Corrosion Lab scheduling assistant!')
    print('############################')
    print()
    id = input('What chamber do you want to view info of: ')
    print()
    chamber_specification = get_chamber_specification(id)
    print('####### CHAMBER INFO #######')
    print()
    display_chamber_specs([chamber_specification])


if __name__ == '__main__':
    run()