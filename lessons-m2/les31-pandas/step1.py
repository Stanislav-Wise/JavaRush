import csv


def read_csv():
    with open('students.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        data = []
        for row in reader:
            name = row[0]
            grade = row[1]
            data.append((name, grade))
    return data[1:]


if __name__ == '__main__':
    print(read_csv())