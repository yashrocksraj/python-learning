# friends=['yash','harshit','banka','rohan']
# for friend in friends:
#   print("Happy new year",friend)
        

# lar_so_far=-1
# print('before',lar_so_far)
# for the_num in [9,4,12,3,74,67]:
#     if the_num > lar_so_far:
#         lar_so_far = the_num
#     # print(lar_so_far,the_num)
# print('After,',lar_so_far)     

# 

# i = 0
# print('before',i)

# for thing in [9,4,12,3,74,67]:
#     i = i + thing
#     print(i,thing)
# print('after',i)    

# print("Average of (9,4,12,3,74,67 is:)")
# count = 0
# sum = 0
# for value in [9,4,12,3,74,67]:
#     count = count + 1
#     sum = sum + value
# print("Average =",sum/count)    

# print('before')
# for value in [9,4,12,3,74,67]:
#     if value > 20:
#         print('large no',value)
# print("after",value)      


# found = False 
# print ('before',found)
# for value in[9,41,12,3,75]:
#     if value == 3:
#         found = True

#     print(found,value)
# print('after',found)

smallest = None 
print('before')
for value in [9,4,12,3,74,67]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)    
    
print('after',smallest)