import sqlite3
from sqlite import DBaction

def prompt():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    print('\n')
    return last_name, first_name

def update_attendance(selection):
    with open('attendance.txt', 'a') as attendance:
        student = ' '.join(selection) + '\n'
        attendance.write(student)

def get_input(dbaction):
    """ Listen indefinitely for scanner input.

    If student's ID numbers is found in the database, update the attendance roster,
    otherwise add the student to the database.
    :param conn: Connection object
    """

    while True:
        student_id = input('')
        c = dbaction.conn.cursor()
        c.execute('SELECT * FROM students WHERE student_id=?', (student_id,))
        selection = c.fetchone()
        if (selection == None):
            name = prompt()
            student = name + (student_id,)
            student_id = dbaction.create_student(student)
            print(f'Student added at ID: {student_id}')
            continue
        else:
            update_attendance(selection)
            print('Attendance updated!')
            continue

def main():
        conn = DBaction('attendance.db')
        conn.create_table()
        print('   AttenDB Beta Version 0.0.1   \n\n')
        get_input(conn)

if __name__ == '__main__':
    main()
