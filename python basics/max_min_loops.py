# largest = None
# print('Before:', largest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if largest is None or itervar > largest :
#         largest = itervar
#     print('Loop:', itervar, largest)
# print('Largest:', largest)


# smallest =None
# print("before:",smallest)

# for i in [3, 41, 12, 9, 74, 15]:
#     if( smallest is None or i < smallest):
#         smallest = i
#     print ("loop:",i,smallest)

# print("smallest",smallest)       



# def smallest(lst):
#     small =None
#     for i in lst:
#        if( small is None or i < small):
#              small = i
    
#     return(small)            

    



# list = [12,89,72,78,97,101,5,24]
# smalll=smallest(list)
# print("smallest:",smalll)


def largest(list):
    largest = None
    for i in list:
      if largest is None or i>largest:
         largest=i
    return largest

list_new=[2,89,75,86,90,91]
large=largest(list_new)
print("largest:",large)


   

