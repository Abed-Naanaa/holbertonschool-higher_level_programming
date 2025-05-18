#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
in a safe way, protecting against SQL injection.
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, db_name, state_name):
    """
    Connects to the MySQL database and lists all cities of the given state
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    query = """SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
