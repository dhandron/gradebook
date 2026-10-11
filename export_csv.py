import csv

from classes import Student

def write_lst_file(file_path, students) -> None:
    with open(file_path, 'w') as file:
        writer = csv.writer(file)

        for student in students:
            entry = []

            entry.append(student.andrew_id)
            entry.append(student.last)
            entry.append(student.first)
            entry.append("C")
            entry.append(student.college + " " + student.department + " " + student.major)
            entry.append(student.section)
            entry.append("")
            entry.append(student.email)
            entry.append(student.andrew_id)
            entry.append("")
            entry.append("0")
            entry.append("")

            
            writer.writerow(entry)


def write_canvas_grade_import(file_path, students):
    with open(file_path, 'w') as file:
        writer = csv.writer(file)

        header = ['Student', 'ID', 'SIS User ID', 'SIS Login ID', 'Section']

       
        header.extend(list(students[0].webwork.grades))
        writer.writerow(header)

        for student in students:
            entry = []

            entry.append(student.canvas_name)
            entry.append(student.canvas_id)
            entry.append(student.sisuserid)
            entry.append(student.sisloginid)
            entry.append(student.canvas_section)

            record = student.webwork.grades
            grades = [record[assignment] for assignment in record]
            entry.extend(grades)

            writer.writerow(entry)

