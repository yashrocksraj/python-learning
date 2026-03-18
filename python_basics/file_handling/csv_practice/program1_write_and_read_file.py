
txt = "My name is yash and i love python"

with open("test.txt", "w") as file:
      file.write(txt)
      file.write("\n")
      file.write("and i will become backend developer")
with open("test.txt","r") as file:
    content = file.read() 
    print(content)  


    