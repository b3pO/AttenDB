import csv
import os
import sqlite3
import sqlite
import time
from sqlite3 import Error
from datetime import date

start_time = time.time()
max_time = 30

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
    """ Takes users first then last name as input and capitalizes the first letter of each.
    """

    first_name = input("Enter student's first name: ")
    first_name = first_name.title()
    last_name = input("Enter student's last name: ")
    last_name = last_name.title()
    print('\n')
    return last_name, first_name

def create_todays_attendance():
    dirs = os.listdir()
    roster = 'attendance.default.csv'
    cmd = 'cp attendance.default.csv `date "+%Y-%m-%d"`.csv'
    if roster not in dirs:
        print('Attendance roster missing!')
    else:
        os.system(cmd)


def update_attendance(selection):
    """ Updates daily attendance roster created by create_todays_attendance().

    :param selection: Tuple consisting of students last_name, first_name
                      as fetched from attendance.db
    """

    t = date.today()
    today = str(t) + '.csv'
    name = list(selection)
    with open(today, 'a', newline='') as attendance:
        fieldnames = ['last_name', 'first_name', 'status']
        writer = writer(attendance, fieldnames=fieldnames)
        for row in reader:
            if row['last_name'] == name[0]:
                writer.writerow({'status': 'PRESENT'})
            else:
                print('Student could not be found on the roster.')

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
            entry_id = create_student(conn, student)
            print(f'Student added at ID: {entry_id}')
        else:
            update_attendance(selection)
            print('Attendance updated!')

#def keep_time():
#    """ Plan is to start the program at 7:45 a.m. and let it run until 8:30 a.m., roughly 45 minutes.
#    """
#    global start_time
#    global max_time

#    while (time.time() - start_time) < max_time:
#        main()

def main():
    create_todays_attendance()
    try:
        with sqlite3.connect('attendance.db') as conn:
            create_table(conn)
            print('   AttenDB Beta Version 0.0.1   \n\n')
            get_input(conn)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
