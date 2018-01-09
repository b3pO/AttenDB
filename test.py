import csv

with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['last_name', 'first_name', 'status']
    writer = csv.DictWriter(csvfile, delimiter=' ', fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'last_name': 'Gay', 'first_name': 'Brandon', 'status': 'ABSENT'})
    writer.writerow({'last_name': 'Smith', 'first_name': 'John', 'status': 'ABSENT'})
    writer.writerow({'last_name': 'Clooney', 'first_name': 'George', 'status': 'ABSENT'})
    writer.writerow({'last_name': 'Pitt', 'first_name': 'Brad', 'status': 'ABSENT'})
    writer.writerow({'last_name': 'Jordan', 'first_name': 'Michael', 'status': 'ABSENT'})
    writer.writerow({'last_name': 'Ramirez', 'first_name': 'Julian', 'status': 'ABSENT'})
