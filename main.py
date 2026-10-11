from classes import AssignmentGroup
from classes import Student
from import_roster import read_roster
from export_csv import write_lst_file
from export_csv import write_canvas_grade_import
from constants import WEBWORK_LST_HEADINGS
from import_webwork import read_webwork
from import_webwork import copy_webwork_to_students
from import_canvas import read_canvas
from import_canvas import get_canvas_assignments
from import_canvas import copy_canvas_to_students
from constants import GROUPS
from constants import CUTOFFS
from cutoffs import generate_cutoff_records




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

students = read_roster("data/241/roster1.csv")
students2 = read_roster("data/241/roster2.csv")
students.extend(students2)
# write_lst_file("data/241/roster.lst", students)



###################

webwork_grades = read_webwork("data/241/webwork.csv")
copy_webwork_to_students(students, webwork_grades)


###################

canvas_record = read_canvas('data/241/canvas.csv')


###################

# for student in students:
#     students[student].webwork = webwork_grades[student]
#     students[student].canvas = canvas_record[student]

# write_canvas_grade_import('data/241/canvas_upload.csv', students)

###################


assignments = get_canvas_assignments("data/241/canvas.csv")
copy_canvas_to_students(students, canvas_record)


for student in students:
    student.compute_cumulative_average()
#     print(f"{student.andrew_id} : {100*student.average}")



cutoffs = generate_cutoff_records()

# for grade in cutoffs:
#     cutoffs[grade].compute_cumulative_average()
#     print(f"The {grade} cutoff is {100 * cutoffs[grade].average}")
#     for group in cutoffs[grade].grades:
#         print(f"The {grade} cutoff for {group.name} is {group.average}")


write_lst_file("data/241/classlist.lst", students)
write_canvas_grade_import("data/241/canvas_upload2.csv", students)

for student in students:
    if student.andrew_id == "bchiu2":
        print(f"{student.first} {student.last} average is {100 * student.average}")
        for group in student.grades:
            print(f"{group.name} average is {100 * group.average}")
            for assignment in group.grades:
                print(f"[{assignment}: {group.grades[assignment]}")



print("done")