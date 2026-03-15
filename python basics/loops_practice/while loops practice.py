while True:
    line = input("yash:")
    if line[0] == "#":
        continue
    if line == "done": 
        break
    print(line)

print ("done!")    

