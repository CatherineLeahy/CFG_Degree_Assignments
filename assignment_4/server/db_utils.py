import random
import string
import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


# signs MySQL and connecting to database
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# gets chamber_specification table from database
def get_chamber_specs():
    try:
        db_name = 'corrosion_lab_equipment'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
                SELECT chamber_id, environment, calibration_due_date FROM chamber_specification;
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


# gets chamber_schedule table and filters by a specific chamber_id
def get_chamber_schedule(chamber_id):
    try:
        db_name = 'corrosion_lab_equipment'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
                SELECT chamber_schedule_id, project_name, start_date, duration, chamber_id FROM chamber_schedule
                WHERE chamber_id = '{}'
                """.format(chamber_id)

        cur.execute(query)

        result = cur.fetchall()
        chamber_schedule = _map_chamber_schedule(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return chamber_schedule


# maps the raw data from the database to a structured dictionary
def _map_chamber_specification(chamber_specification):
    mapped = []
    for item in chamber_specification:
        mapped.append({
            'chamber_id': item[0],
            'environment': item[1],
            'calibration_due_date': item[2]})
    return mapped


# maps the raw data from the database to a structured dictionary
def _map_chamber_schedule(chamber_schedule):
    mapped = []
    for item in chamber_schedule:
        mapped.append({
            'chamber_schedule_id': item[0],
            'project_name': item[1],
            'start_date': item[2],
            'duration': item[3],
            'chamber_id': item[4]})
    return mapped


# adds a new project to chamber_schedule table
def schedule_new_project(project_name, start_date, duration, chamber_id):
    try:
        try:
            db_name = 'corrosion_lab_equipment'
            db_connection = _connect_to_db(db_name)
            cur = db_connection.cursor()
            print("Connected to DB: %s" % db_name)

            query = """
                    INSERT INTO chamber_schedule
                    (chamber_schedule_id,project_name,start_date,duration,chamber_id)
                    VALUES
                    ('{}','{}','{}','{}','{}')
                    """.format(_generate_random_id(), project_name, start_date, duration, chamber_id)

            cur.execute(query)
            db_connection.commit()
            cur.close()

        except Exception:
            raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()


# generates a random alpha numeric ID for the primary key chamber_schedule_id
def _generate_random_id():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return x