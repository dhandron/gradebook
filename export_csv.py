import csv

from classes import Student

def write_lst_file(file_path, data) -> None:
    with open(file_path, 'w') as file:
        writer = csv.writer(file)

        for id in data:
            entry = []

            entry.append(data[id].andrew_id)
            entry.append(data[id].last)
            entry.append(data[id].first)
            entry.append("C")
            entry.append(data[id].college + " " + data[id].department + " " + data[id].major)
            entry.append(data[id].section)
            entry.append("")
            entry.append(data[id].email)
            entry.append(data[id].andrew_id)
            entry.append("")
            entry.append("0")
            entry.append("")

            
            writer.writerow(entry)


def write_canvas_grade_import(file_path, students):
    with open(file_path, 'w') as file:
        writer = csv.writer(file)

        header = ['Student', 'ID', 'SIS User ID', 'SIS Login ID', 'Section']

        id = list(students)[0]
        header.extend(list(students[id].webwork))
        writer.writerow(header)

        for id in students:
            entry = []

            entry.append(students[id].canvas['Student'])
            entry.append(students[id].canvas['ID'])
            entry.append(students[id].canvas['SIS User ID'])
            entry.append(students[id].canvas['SIS Login ID'])
            entry.append(students[id].canvas['Section'])

            record = students[id].webwork
            grades = [record[assignment] for assignment in record]
            entry.extend(grades)

            writer.writerow(entry)

