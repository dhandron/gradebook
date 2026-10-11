

def assign_grades(students, cutoffs):
    for student in students:
        if student.average >= cutoffs["A"].average:
            student.letter_grade = "A"
        elif student.average >= cutoffs["B"].average:
            student.letter_grade = "B"
        elif student.average >= cutoffs["C"].average:
            student.letter_grade = "C"
        elif student.average >= cutoffs["D"].average:
            student.letter_grade = "D"
        else:
            student.letter_grade = "R"

def assign_midsemester_grades(students, cutoffs):
    for student in students:
        if student.average >= (cutoffs["A"].average + 1)/2:
            student.letter_grade = "A"
        elif student.average >= cutoffs["A"].average:
            student.letter_grade = "A-"
        elif student.average >= (cutoffs["B"].average + 2 * cutoffs["A"].average)/3:
            student.letter_grade = "B+"
        elif student.average >= (2 * cutoffs["B"].average + cutoffs["A"].average)/3:
            student.letter_grade = "B"
        elif student.average >= cutoffs["B"].average:
            student.letter_grade = "B-"
        elif student.average >= (cutoffs["C"].average + 2 * cutoffs["B"].average)/3:
            student.letter_grade = "C+"
        elif student.average >= (2 * cutoffs["C"].average + cutoffs["B"].average)/3:
            student.letter_grade = "C"
        elif student.average >= cutoffs["C"].average:
            student.letter_grade = "C-"
        elif student.average >= (cutoffs["D"].average + cutoffs["C"].average)/2:
            student.letter_grade = "D+"
        elif student.average >= cutoffs["D"].average:
            student.letter_grade = "D"
        else:
            student.letter_grade = "R"
