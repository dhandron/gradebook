from classes import Course
from classes import AssignmentGroup
from classes import Student
from import_roster import read_roster
from export_csv import write_lst_file
from export_csv import write_canvas_grade_import
from constants import WEBWORK_LST_HEADINGS
from import_webwork import read_webwork
from import_canvas import read_canvas
from import_canvas import get_canvas_assignments
from constants import GROUPS
from constants import CUTOFFS



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

students = read_roster("data/roster.csv")
# students2 = read_roster("data/241/roster2.csv")
# students = students1 | students2
# write_lst_file("data/241/roster.lst", students)



###################

# webwork_grades = read_webwork("data/241/webwork.csv")
# print(webwork_grades)


###################

canvas_record = read_canvas('data/canvas.csv')


###################

# for student in students:
#     students[student].webwork = webwork_grades[student]
#     students[student].canvas = canvas_record[student]

# write_canvas_grade_import('data/241/canvas_upload.csv', students)

course = Course("21-241", "Matrices and Linear Transformations", "Fall 2026")


assignments = get_canvas_assignments("data/canvas.csv")


for group in GROUPS:
    group_assignments = []
    prefix_length = len(group["prefix"])
    for assignment in assignments:
        if assignment[:prefix_length] == group["prefix"]:
            group_assignments.append(assignment)
    for student in students:
        grade_record = AssignmentGroup(group["name"], group["weight"])
        for assignment in group_assignments:
            grade_record.grades[assignment] = (canvas_record[student.andrew_id][assignment], assignments[assignment])
        student.grades.append(grade_record)

for student in students:
    student.compute_cumulative_average()
    print(f"{student.andrew_id} : {100*student.average}")

for group in GROUPS:
    group_assignments = []
    prefix_length = len(group["prefix"])
    for assignment in assignments:
        if assignment[:prefix_length] == group["prefix"]:
            group_assignments.append(assignment)
    grade_cutoffs = {}
    for grade in ["A", "B", "C", "D"]:
        cutoff_record = Student(grade, None, None, '', '', '', '', None)
        grade_record = AssignmentGroup(group["name"], group["weight"])
        for assignment in group_assignments:
            if assignment in CUTOFFS:
                grade_record.grades[assignment] = (CUTOFFS[assignment], assignments[assignment])
            else:
                grade_record.grades[assignment] = (CUTOFFS["default"], assignments[assignment])
        cutoff_record.grades.append(grade_record)
    grade_cutoffs[grade] = cutoff_record


print(len(grade_cutoffs["D"].grades))


print("done")