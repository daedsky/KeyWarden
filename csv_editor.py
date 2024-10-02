import csv


def create_empty_csv(fp, headers: list):
    with open(fp, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)


def append_csv(fp, data: list):
    with open(fp, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(data)


def read_csv(fp):
    csv_file = open(fp, 'r', newline='', encoding='utf_8_sig')
    csv_reader = csv.DictReader(csv_file)

    return csv_file, csv_reader


