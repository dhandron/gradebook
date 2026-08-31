import csv

from studentclass import Student

def read_roster(file_path):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)

        students = {}
        for row in reader:
            students[row["Andrew ID"]] = Student(row["Andrew ID"], 
                                    row["Preferred/First Name"], 
                                    row["Last Name"],
                                    row["College"],
                                    row["Department"],
                                    row["Major"],
                                    row["Section"],
                                    row["Email"],
                                    )

    return students