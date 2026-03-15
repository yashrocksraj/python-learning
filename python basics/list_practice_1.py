#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list1=[1,2,3,2,1]
list2=[1,"abc","abc",1]
copy_list1=list1.copy()
copy_list2=list2.copy()
copy_list1.reverse()
copy_list2.reverse()
if((copy_list1==list1),copy_list2==list2):
    print("list 1 is palindrome")  
    print("list 2 is palindrome")
else:
    print("lists are not palindrome")

