#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa with their state names."""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Connects to the database and lists all cities with their corresponding states.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
