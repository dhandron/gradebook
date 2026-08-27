import csv

def open_reader(file_path):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
    return reader

def open_writer(file_path):
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
    return writer

