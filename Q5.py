'''
5. Provide a program to create tables (Employee, Department,
Project) in database Sqlite and insert the data.
• Make sure to add basic field, with employee to department and project relation.
• Make sure maintain M2M relation between employee and project.
'''

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


import sqlite3


def insertVaribleIntoEmployee(conn, Employee_id, name, city, DEPT_NO):
    try:
        c = conn.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO Employee
                          ( Employee_id, name, city, DEPT_NO) 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (Employee_id, name, city, DEPT_NO)
        c.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into Employee table")

        c.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if c:
            c.close()
            print("The SQLite connection is closed")


def insertVaribleIntoProjects(conn, Project_id, Project_name, Employee_id):
    try:
        c = conn.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO projects
                          (Project_id ,Project_name,Employee_id) 
                          VALUES (?, ?, ?);"""

        data_tuple = (Project_id, Project_name, Employee_id)
        c.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into Projects table")

        c.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if c:
            c.close()
            print("The SQLite connection is closed")


def insertVaribleIntoDepartment(conn, DEPT_NO, DEPT_NAME, LOCATION):
    try:
        c = conn.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO Department
                          (DEPT_NO, DEPT_NAME, LOCATION) 
                          VALUES (?, ?, ?);"""

        data_tuple = (DEPT_NO, DEPT_NAME, LOCATION)
        c.execute(sqlite_insert_with_param, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into Department table")

        c.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if c:
            c.close()
            print("The SQLite connection is closed")


def main():
    database = r"pythonsqlite.db"

    sql_create_Employee_table = """ CREATE TABLE IF NOT EXISTS Employee(
                                     Employee_id integer(5) PRIMARY KEY, 
                                     name char(30)NOT NULL, 
                                     city char(35),
                                     DEPT_NO char(3)
                                     );"""
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                         Project_id integer(10) PRIMARY KEY,
                                         Project_name char(40),
                                         Employee_id integer(5)
                                     );"""

    sql_create_Department_table = """
                                CREATE TABLE IF NOT EXISTS Department(
                                DEPT_NO char(3) NOT NULL,
                                DEPT_NAME  char(29) NOT NULL,
                                LOCATION  char(16) PRIMARY KEY 
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Employ table
        create_table(conn, sql_create_Employee_table)
        insertVaribleIntoEmployee(conn, 2, 'Joe', 'ghazipur', '02')
        insertVaribleIntoEmployee(conn, 3, 'Ben', 'varanasi', '04')
        # create projects table
        create_table(conn, sql_create_projects_table)
        insertVaribleIntoProjects(conn,232,"My4C",2)
        insertVaribleIntoProjects(conn, 242, "Bd's", 3)
        # create tasks table
        create_table(conn, sql_create_Department_table)
        insertVaribleIntoDepartment(conn,'34','Dilivery','Jaipur')
        insertVaribleIntoDepartment(conn, '30', 'Dev', 'Gurgava')
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
