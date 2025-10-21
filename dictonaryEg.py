#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
a=input("enter first subject: ")
a_marks=int(input("enter marks of first subject: "))
b=input("enter second subject: ")
b_marks=int(input("enter marks of second subject: "))
c=input("enter third subject: ")
c_marks=int(input("enter marks of third subject: "))
dic={}
dic[a]=a_marks
dic[b]=b_marks
dic[c]=c_marks
print(dic)