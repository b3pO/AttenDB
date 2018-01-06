import sqlite3
from sqlite3 import Error

class DBaction:
    """ SQLite actions and manipulations.

    __init__        :   parameters=db_file; creates db connection
    create_table    :   parameters=connection; creates table; returns None
    create_student  :   parameters=connection, student(last_name, first_name, student_id);
                        creates student object; returns student_id in table
    """
    def __init__(self, db_file):
        """ Create an SQLite database connection specified by the db_file

        :param db_file: database file
        :return: Connection object
        """
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return None

    def create_table(self):
        """ Create a table using a CREATE TABLE statement

        :param conn: Connection object
        """

        try:
            c = self.conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS students
                            (last_name text, first_name text, student_id text)''')
            self.conn.commit()
        except Error as e:
            print(e)

    def create_student(self, student):
        """ Create a new student into the students table

        :param conn: Connection object
        :param student: Tuple of strings representing fields in the table
        """

        sql = ('''INSERT INTO students(last_name, first_name, student_id) VALUES(?,?,?)''')
        c = self.conn.cursor()
        c.execute(sql, student)
        self.conn.commit()
        return c.lastrowid
