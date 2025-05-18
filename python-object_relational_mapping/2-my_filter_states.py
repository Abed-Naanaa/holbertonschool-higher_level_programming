#!/usr/bin/python3
"""Displays all values in the states table matching a given name."""

import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    """
    Connects to the database and prints states where name matches user input.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): State name to search.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_name(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )
