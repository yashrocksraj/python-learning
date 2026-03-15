data =["name","age","marks"]
with open("my_first_csv_file.csv","w") as csv_file_1st:
    content = csv_file_1st.write(",".join(data))
    print(content)