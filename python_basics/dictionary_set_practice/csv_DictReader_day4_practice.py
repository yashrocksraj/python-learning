# Problem 1
# Read a CSV file 
# import csv
# with open("python_basics/program_files/olympics.txt","r") as f:
#    reader = csv.reader(f)
#    next(reader)
#    for row in reader:
#      if row[3] == "China":
#         print(f"{row[0]} is from China")
#----------------#----------------#     
# Problem 2
# Read CSV file using DictReader

import csv
with open("python_basics/program_files/olympics.txt","r") as f:
   reader = csv.DictReader(f)
   count = 0
   for row in reader:
     if row["Team"] == "China":
        print(f"{row["Name"]} is from China")
        count+=1
print("Total Players from China:",count)   
#----------------#----------------#
# Problem 3
# Count medals from file     
import csv
with open("python_basics/program_files/olympics.txt","r") as f:
   reader = csv.DictReader(f)
   medals = {}
   
   for row in reader:
      medal = row["Medal"]
      if medal not in medals:
         medals[medal] = 0
      medals[medal]+=1    

   total_medals = 0   
   
   for key in sorted(medals):
      if key != "NA":
       total_medals = total_medals + medals[key]
       print(f"{key}:{medals[key]}")  
   
   print(f"Total medals:{total_medals}")      
# ----------------#----------------#
# Problem 4
# Find Most Frequent medal
import csv
with open("python_basics/program_files/olympics.txt","r") as f:
   reader = csv.DictReader(f)
   medals = {}          
   for row in reader:
      medal = row["Medal"]
      if medal not in medals:
         medals[medal] = 0
      medals[medal] += 1
   
   max_medal = ""
   max_value = 0
   for key in sorted(medals):
      if key != "NA":
         if medals[key] > max_value:
            max_value = medals[key]
            max_medal = key
print(f"most frequent medal is : {max_medal} , value: {max_value}") 
# ----------------#----------------#

      
    
         
