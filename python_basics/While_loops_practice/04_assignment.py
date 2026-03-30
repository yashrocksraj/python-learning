# Assignment 4 - While loops

# Problem 1: Sublist
def sublist(num_lst:list):
    sub_lst = []
    x = 0

    while x < len(num_lst):
        if num_lst[x]== 5:
            x += 1
            break
        else:
            sub_lst.append(num_lst[x])
            x +=1
    return sub_lst        

# Problem 2: check_nums
lst1 = [0,1,2,3,4,5]
print(sublist(lst1))

def check_nums(num_list:list):
    x = 0 
    while x < len(num_list):
        if num_list[x] == 7:
            num_list.pop(x)
            return num_list
        x += 1
    return num_list


# Problem 3: sublist STOP
def sublist(string_list:list):
    x = 0
    while x < len(string_list):
        if string_list[x].upper() == "STOP":
            return string_list[:x]
        x += 1
    return string_list

list1 = ["hi","hey","hello","holla","stop"]
print(sublist(list1))


# Problem 4: stop_at_z
def stop_at_z(string_list:list):
    new_list = []
    x = 0
    while x < len(string_list):
        if string_list[x].lower() == 'z':
            return new_list
        else:
            new_list.append(string_list[x])
        x += 1
    return string_list


# Problem 5: write sum program for both for and while loop
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

x= 0
sum2 = 0
while x < len(lst):
    sum2 = sum2 + lst[x]
    x += 1
    

# Problem 6: Begninng and bye
def beginning(str_lst:list):
    x = 0 
    while x < len(str_lst):
        if str_lst[x] == 'bye':
            return str_lst[:min(x,10)]
        
        if x == 10:
            return str_lst[:10]
        
        x += 1
        
    return str_lst[:10]    
            