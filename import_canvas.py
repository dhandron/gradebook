import csv

from constants import GROUPS
from classes import AssignmentGroup

def get_canvas_assignments(file_path):
    # returns a dictionary
    # keys are assignment names
    # values are the maximum possible points for the assignment
    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        header_row = next(reader)
        max_points_row = next(reader)
        
        column = 6
        assignments = {}
        # print(row)
        while max_points_row[column].strip() != "(read only)":
            assignments[header_row[column].split(' (', maxsplit=1)[0].strip()] = max_points_row[column]
            column += 1

        return assignments


def read_canvas(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        row = next(reader)
        while row[0].strip() != "Points Possible":
            row = next(reader)

        
        i = 0
        # print(row)
        while row[i].strip() != "(read only)":
            # print(i, row[i])
            i += 1

        end = i

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        keys = next(reader)

        next(reader)

        records = {}
        for row in reader:
            andrew_id = row[3].split('@', maxsplit=1)[0].strip()
            records[andrew_id] = {keys[i].split(' (', maxsplit=1)[0].strip(): row[i] for i in range(end)}

    #print(records)
    return records


def copy_canvas_to_students(students, canvas_record):
    assignments = get_canvas_assignments("data/241/canvas.csv")

    for student in students:
        student.canvas_name = canvas_record[student.andrew_id]["Student"]
        student.canvas_id = canvas_record[student.andrew_id]["ID"]
        student.sisuserid = canvas_record[student.andrew_id]["SIS User ID"]
        student.sisloginid = canvas_record[student.andrew_id]["SIS Login ID"]
        student.rootaccount = canvas_record[student.andrew_id]["Root Account"]
        student.canvas_section = canvas_record[student.andrew_id]["Section"]

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