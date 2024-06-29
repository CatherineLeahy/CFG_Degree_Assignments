import mysql.connector
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


def get_chamber_infos():
    try:
        db_name = 'lab'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
                SELECT chamber_info_id, capacity FROM chamber_info;
                """

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        chamber_info = _map_chamber_info(result)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return chamber_info

def _map_chamber_info(chamber_info):
    mapped = []
    for item in chamber_info:
        mapped.append({
            'id': item[0],
            'capacity': item[1],
        })
    return mapped