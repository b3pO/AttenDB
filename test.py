import csv

with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'last_name': 'Gay', 'first_name': 'Brandon', })
    writer.writerow({'last_name': 'Doe', 'first_name': 'John'})
