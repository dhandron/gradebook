import csv

def read_webwork(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        row = next(reader)
        # print(row)
        while row[0][:8] != "SET NAME":
            # print(row[0][:8] + '.')
            row = next(reader)
        keys = row

        for i in range(1,len(keys)):
            if keys[i].strip():
                # print(f"first assignment in column {i}")
                break
       
        start = i
        # print(f"start is {i}")

        for i in range(start, len(keys)):
            if keys[i][:7] == "summary":
                # print(f"summary in column {i}")
                break

        end = i
        # print(f"end is {i}")

        # print(f"assignments are {row[start:end]}")

        while row[0][:10] != "STUDENT ID":
            row = next(reader)

        grades = {}
        for row in reader:
            grades[row[0].strip()] = {keys[i].strip(): float(row[i]) for i in range(start, end)}

        return grades
        
        