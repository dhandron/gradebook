import csv

def get_canvas_assignments(file_path):
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