import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Create an SQLite database connection specified by the db_file

    :param db_file: database file
    :return: Connection object
    """

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def create_table(conn):
    """ Create a table using a CREATE TABLE statement

    :param conn: Connection object
    """

    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS students
                        (last_name text, first_name text, student_id text)''')
        conn.commit()
    except Error as e:
        print(e)

def create_student(conn, student):
    """ Create a new student into the students table

    :param conn: Connection object
    :param student: Tuple of strings representing fields in the table
    """

    sql = ('''INSERT INTO students(last_name, first_name, student_id) VALUES(?,?,?)''')
    c = conn.cursor()
    c.execute(sql, student)
    conn.commit()
    return c.lastrowid

def prompt():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    print('\n')
    return last_name, first_name

def update_attendance(selection):
    with open('attendance.txt', 'a') as attendance:
        student = ' '.join(selection) + '\n'
        attendance.write(student)

def get_input(conn):
    """ Listen indefinitely for scanner input.

    If student's ID numbers is found in the database, update the attendance roster,
    otherwise add the student to the database.
    :param conn: Connection object
    """

    while True:
        student_id = input('')
        c = conn.cursor()
        c.execute('SELECT * FROM students WHERE student_id=?', (student_id,))
        selection = c.fetchone()
        if (selection == None):
            name = prompt()
            student = name + (student_id,)
            student_id = create_student(conn, student)
            print(f'Student added at ID: {student_id}')
            continue
        else:
            update_attendance(selection)
            print('Attendance updated!')
            continue

if __name__ == '__main__':
    conn = create_connection('attendance.db')
    create_table(conn)
    print('   AttenDB Beta Version 0.0.1   \n\n')
    get_input(conn)
