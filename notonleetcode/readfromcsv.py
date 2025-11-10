import csv

with open('data.csv', newline='') as fp:
    reader = csv.reader(fp)

    next(reader)

    values = []
    for row in reader:
        values.append(row[1])

    
print(values)
