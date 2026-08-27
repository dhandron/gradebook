import csv

from studentclass import Student


# with open("data/roster.csv", newline='') as f:
#     with open('data/roster.lst', 'w') as file:
#         reader = csv.DictReader(f)
#         writer = csv.writer(file)
#         for row in reader:
#             entry = []
#             entry.append(row["Andrew ID"])
#             entry.append(row["Last Name"])
#             entry.append(row["Preferred/First Name"])
#             entry.append("C")
#             entry.append(row["College"] + " " + row["Department"] + " " + row["Major"])
#             entry.append(row["Section"])
#             entry.append("")
#             entry.append(row["Email"])
#             entry.append(row["Andrew ID"])
#             entry.append("")
#             entry.append("0")
#             entry.append("")
            
#             writer.writerow(entry)

with open("data/roster.csv", newline='') as f:
    reader = csv.DictReader(f)

    students = []
    for row in reader:
        students.append(Student(row["Andrew ID"], row["Preferred/First Name"], row["Last Name"]))

for student in students:
    print(student.andrew_id, student.first, student.last)

print("done")