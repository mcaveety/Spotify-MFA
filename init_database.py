# Code from https://www.sqlitetutorial.net/sqlite-python/create-tables/
# Creates user table in database file for storage of data using SQLite3

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "database.db"

    create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        username text NOT NULL UNIQUE,
                                        password text NOT NULL,
                                        mobile_number text NOT NULL UNIQUE
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # Try to create table
    if conn is not None:
        # Create users table
        create_table(conn, create_users_table)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
