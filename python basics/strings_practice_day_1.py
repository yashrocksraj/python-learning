#--------print each character in a string using while and for loop--------- 

# fruit = 'apple'
# i = 0
# while( i < len(fruit)):
#     letter = fruit[i]
#     print(i,letter)
#     i = i + 1


# f = 'banana'
# for ind in f:
#     print(ind)    

#---------------------counting and looping in a string----------------#

# name = 'yash raj'
# count = 0
# for i in name:
#     if i== 'a':
#         count = count + 1
# print(count)         

#-----------slicing in a string--------------#

# name = 'yash raj yadav'
# print(name[2:10])
# print(name[0:15])
# print(name[6:7])


# using in as logical operator

# fruit = 'banana'
# if 'n' in fruit:
#     print('found it')
 
#-------------------parsing and extracting-----------------#

# data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# # atpos = data.find('@')
# # print(atpos)

# # sspo = data.find(' ',atpos)
# # print(sspo)

# # host = data[atpos+1:sspo]
# # print(host)

# atpos = data.find('5')
# print(atpos)

# sspos = data.find(' ',atpos)
# print(sspos)
# host = data[sspos+1:]
# print(host)

#--------------------------------practice questions--------------#

# Exercise 5: Slicing strings 
# Take the following Python code that stores a string: str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and
# then use the float function to convert the extracted string into a floating point number.

# str = 'X-DSPAM-Confidence: 0.8475'
# data = str.find(':')
# print(data)
# host = (str[data+2:])
# print(float(host),type(float(host)))


# text = "Learning Python is fun"
# print(text.upper())
# print(text.lower())
# print(len(text))
# print(text[0:1])
# print(text[21:22])

city = 'New Delhi'
print(city[0:3])
print(city[4:])