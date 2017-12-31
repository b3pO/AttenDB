import dbm
import pickle

def prompt():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    full_name = (last_name, first_name)
    return full_name

def update_attendance(student_id):
    with open('attendance.txt', 'w') as attendance:
        attendance.write(student_id)

def get_input():
    while True:
        student_id = input('')
        with dbm.open('attendance', 'c') as db:
            values = [db[key] for key in db.keys()]
            if student_id not in values:
                global full_name
                full_name = prompt()
                pickled = pickle.dumps(full_name)
                db[pickled] = student_id
                print('Stored!')
                continue
            else:
                update_attendance(student_id)

if __name__ == '__main__':
    print('   AttenDB Beta Version 0.0.1   \n\n')
    get_input()
