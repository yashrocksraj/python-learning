# Problem 1
# Print count of all the letters and characters in the file and assigned them to a dictionary.

f = open("python basics/program_files/Scarlet.txt","r")
letters = f.read()
letters_count = {}
for ch in letters:
    letters_count[ch] = letters_count.get(ch,0) + 1
for ch in sorted(letters_count):
    print(ch + ":" + str(letters_count[ch]))
# #----------------------------#

# Problem 2
# Count only spaces in the file
    
space_count = 0
for ch in letters:
    if ch == " " :
        space_count += 1
print("space_count:",space_count)        
# #----------------------------#

# Problem 3
# count no of 'a' in a file both using dict and conditionals.

a_count = 0
for ch in letters:
    if ch == 'a':
        a_count += 1
print("'a' count :",letters_count['a'])      
# #----------------------------#  

f.close()

