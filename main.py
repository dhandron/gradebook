from classes import Course
from import_roster import read_roster
from export_csv import write_lst_file
from export_csv import write_canvas_grade_import
from constants import WEBWORK_LST_HEADINGS
from import_webwork import read_webwork
from import_canvas import read_canvas

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

###################

students1 = read_roster("data/241/roster1.csv")
students2 = read_roster("data/241/roster2.csv")
students = students1 | students2
write_lst_file("data/241/roster.lst", students)

###################

# webwork_grades = read_webwork("data/241/webwork.csv")
# print(webwork_grades)


###################

canvas_record = read_canvas('data/canvas.csv')
for key in canvas_record:
    print(key)

###################

# for student in students:
#     students[student].webwork = webwork_grades[student]
#     students[student].canvas = canvas_record[student]

# write_canvas_grade_import('data/241/canvas_upload.csv', students)

course = Course("21-241", "Matrices and Linear Transformations", "Fall 2026")

course.roster = []
for id in students:
    course.roster.append(students[id])

for student in course.roster:
    print(student.first + " " + student.last)

print("done")