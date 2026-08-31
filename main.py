from studentclass import Student
from import_roster import read_roster
from export_csv import write_lst_file
from constants import WEBWORK_LST_HEADINGS

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

students = read_roster("data/roster.csv")
write_lst_file("data/roster.lst", students)

 
for id in students:
    print(students[id].andrew_id, students[id].first, students[id].last)

print("done")