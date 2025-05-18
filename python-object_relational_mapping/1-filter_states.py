#!/usr/bin/python3
"""Lists all states with a name starting with 'N' from the database."""

import MySQLdb
import sys


def filter_states_starting_with_n(username, password, database):
    """Connects to the database and prints states starting with 'N'."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_starting_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
