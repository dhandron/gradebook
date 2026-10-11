from constants import GROUPS
from constants import CUTOFFS
from classes import Student
from classes import AssignmentGroup
from import_canvas import get_canvas_assignments

def generate_cutoff_records():
    assignments = get_canvas_assignments("data/canvas.csv")
    cutoff_records = {}
    for grade in ["A", "B", "C", "D"]:
        cutoff_records[grade] = Student(grade, None, None, '', '', '', '', None)

    for group in GROUPS:
        group_assignments = []
        prefix_length = len(group["prefix"])
        for assignment in assignments:
            if assignment[:prefix_length] == group["prefix"]:
                group_assignments.append(assignment)
        for grade in cutoff_records:
            grade_record = AssignmentGroup(group["name"], group["weight"])
            for assignment in group_assignments:
                if assignment in CUTOFFS:
                    grade_record.grades[assignment] = (CUTOFFS[assignment][grade], 100)
                else:
                    grade_record.grades[assignment] = (CUTOFFS["default"][grade], 100)

            cutoff_records[grade].grades.append(grade_record)
    return cutoff_records