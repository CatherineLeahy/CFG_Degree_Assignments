import mysql.connector
from datetime import timedelta
# from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='abcd1234',
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def get_chamber_specs():
    try:
        db_name = 'corrosion_lab_equipment'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
                SELECT chamber_id, capacity, environment, calibration_due_date FROM chamber_specification;
                """

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        chamber_specification = _map_chamber_specification(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return chamber_specification

def _map_chamber_specification(chamber_specification):
    mapped = []
    for item in chamber_specification:
        mapped.append({
            'id': item[0],
            'capacity': item[1],
            'environment': item[2],
            'calibration_due_date': item[3] })
    return mapped

# method for listing available chambers based on user inputs of sample quantity, duration and environment
def get_chamber_availability():
    try:
        db_name = 'corrosion_lab_equipment'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """"
                SELECT chamber_id, capacity, environment, calibration_due_date
                FROM chamber_specification
                WHERE capacity >= %s AND environment = %s
                """

        cur.execute(query, (sample_quantity, environment))
        result = cur.fetchall()
        chamber_specification = _map_chamber_specification(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

    available_chambers = [] # create empty list
    for chamber in chamber_specification: # loops through each chamber
        if _is_chamber_available(chamber['chamber_id'], duration):
            available_chambers.append(chamber)
    return available_chambers

# method for qualifying if a chamber is available
def _is_chamber_available():




