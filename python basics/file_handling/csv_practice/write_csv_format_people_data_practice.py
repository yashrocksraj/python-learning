import csv

data =[
    ["Yash",28,"6.4 cgpa"],
    ["Raj",34,"7.9 cgpa"],
    ["Siya",22,"5.9 cgpa"]
]

with open("people_data.csv","w",newline ="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age","Cgpa"])
    for i in data:
        writer.writerow(i)
