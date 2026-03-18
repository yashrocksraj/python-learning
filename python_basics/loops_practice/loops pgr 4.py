# #Print the elements of the following list using a loop:[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for val in list:
#     print(val)




 #Search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81,100)\

list=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=49
idx=0
for num in list:
    if(num==x):
        print("number found",idx)
        break
    idx+=1
    