import requests


def get_chamber_info(id):
    result = requests.get(
        'http://127.0.0.1:5001/chamber/{}'.format(id),
        headers={'content-type': 'application/json'}
    )
    return result.json()


def display_chamber_infos(chamber_info):
    # Print the names of the columns.
    print("{:<15} {:<15}".format(
        'ID', 'Capacity'))
    print('-' * 30)

    # print each data item.
    for item in chamber_info:
        print("{:<15} {:<15}".format(
            item['id'], item['capacity']
        ))


def run():
    print('############################')
    print('Hello, welcome to our lab')
    print('############################')
    print()
    id = input('What chamber do you want to view info of: ')
    print()
    chamber_info = get_chamber_info(id)
    print('####### CHAMBER INFO #######')
    print()
    display_chamber_infos([chamber_info])


if __name__ == '__main__':
    run()