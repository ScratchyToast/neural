import csv

columns = []
with open('D:\ALL\dmg2.csv',encoding="UTF-8") as f: 
    reader = csv.reader(f)
    for row in reader:
        if columns:
            for i, value in enumerate(row):
                columns[i].append(value)
        else:
            columns = [[value] for value in row]
as_dict = {c[0] : c[1:] for c in columns}
print(as_dict)
