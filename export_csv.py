import csv

def write_lst_file(file_path:str, data:{str:Student}) -> None:
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


