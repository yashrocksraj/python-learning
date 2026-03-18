outfile = open("introduction_text.txt","r")
content = outfile.readlines() 
print(content)
three = []

for ch in content:
    three.append(ch[0])
print(three)
outfile.close()    


