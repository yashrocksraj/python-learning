# ques 1
# create a new list containing: squares of all numbers

nums =[1,4,9,16,25]
nums_sq = [num*num for num in nums]
print(nums_sq)

# Ques 2.
# Create a list containing: only numbers divisible by 10

nums1 = [10,20,30,65,85,23]
nums_div_10 = [num for num in nums1 if num%10 == 0]
print(nums_div_10)

# Ques 3.
# Using map() and lambda: convert all words to uppercase.
words = ["python","backend","api"]
words_upper = list(map(lambda word : word.upper(),words))
print(words_upper)

# Ques 4.
# Using filter() and lambda: keep only words whose length is greater than 3.
words = ["cat","elephant","dog","developer","api"]
filter_words = list(filter(lambda word:len(word)>3,words))
print(filter_words)

# Ques 5.
# Using Zip print name , score
names = ["Yash","Rahul","Aman"]
marks = [90,45,80]
for name,marks in zip(names,marks):
    print(name,marks)

# Ques 6.
# Create a new list containing: sum of corresponding elements    
nums1 = [1,2,3]
nums2 = [4,5,6]
sum_list = [x1+x2 for x1,x2 in zip(nums1,nums2)]
print(sum_list)

# Ques 7.
# Using:zip filter lambda Keep only students whose marks > 50.
names = ["Yash","Rahul","Aman","Karan"]
marks = [95,40,82,30]
marks_50 = list(filter(lambda x :x[1]>50,zip(names,marks) ))
print(marks_50)

# Ques 8.
# create dict for key users and emails from lists

users = ["yash","rahul","aman"]

emails = [
    "y@gmail.com",
    "r@gmail.com",
    "a@gmail.com"
]

result=[{'user':user,'email':email} 
    for user,email in zip(users,emails)]
   
print(result)   
         
# Bonuse challenge add age to it.

ages = [22,24,21]

users = ["yash","rahul","aman"]

emails = [
    "y@gmail.com",
    "r@gmail.com",
    "a@gmail.com"
]

result=[{'user':user,'email':email,'age':age} 
    for user,email,age in zip(users,emails,ages)]
   
print(result)




