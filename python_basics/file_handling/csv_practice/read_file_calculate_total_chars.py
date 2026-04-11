outfile = open("C:\Python-learning\python_basics\program_files\introduction_text.txt","r")
content = outfile.readlines() 
print(content)
three = []

for ch in content:
    three.append(ch[0])
print(three)
outfile.close()    


