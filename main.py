from classes import Course
from classes import AssignmentGroup
from import_roster import read_roster
from export_csv import write_lst_file
from export_csv import write_canvas_grade_import
from constants import WEBWORK_LST_HEADINGS
from import_webwork import read_webwork
from import_canvas import read_canvas
from import_canvas import get_canvas_assignments
from constants import HW_WEIGHT
from constants import WW_WEIGHT
from constants import MIDTERM_WEIGHT
from constants import FINAL_WEIGHT


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
hw = []
ww = []
midterms = []
final = []
for assignment in assignments:
    if assignment[:2] == "HW" and assignment != "HW#0":
        hw.append(assignment)
    elif assignment[:2] == "WW":
        ww.append(assignment)    
    elif assignment[:4] == "Exam":
        midterms.append(assignment)
    elif assignment[:5] == "Final":
        final.append(assignment)
    # else:
    #     print(assignment)
   


for student in students:
    student.online_hw = AssignmentGroup("WebWork", WW_WEIGHT)
    for assignment in ww:
        student.online_hw.grades[assignment] = float(canvas_record[student.andrew_id][assignment])
    student.written_hw = AssignmentGroup("WebWork", HW_WEIGHT)
    for assignment in hw:
        student.written_hw.grades[assignment] = float(canvas_record[student.andrew_id][assignment])
    student.midterms = AssignmentGroup("Midterm Exams", MIDTERM_WEIGHT)
    for assignment in midterms:
        student.midterms.grades[assignment] = float(canvas_record[student.andrew_id][assignment])
    student.final = AssignmentGroup("Final Exam", FINAL_WEIGHT)
    for assignment in final:
        if isinstance(canvas_record[student.andrew_id][assignment], float):
            student.final.grades[assignment] = float(canvas_record[student.andrew_id][assignment])
        else:
            student.final.grades[assignment] = 0
student = students[0]
print(student.online_hw.grades)
student.online_hw.compute_average()
print(student.online_hw.average)


# print(student.written_hw.grades)
# print(student.midterms.grades)
# print(student.final.grades)




print("done")