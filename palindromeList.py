#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

#hint: [1, 2, 3, 2, 1] and [1,“abc”,“abc”, 1]
list=[1,2,3,2,1]
list_cpy=list.copy()
list.reverse()
if(list==list_cpy):
    print ("palindrome")
else:
    print("not palindrome")