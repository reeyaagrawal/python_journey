#WAP to find the greatest of 3 numbers entered by the user.
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if(a>=b and a>=c):
    print(a," is greatest")
elif(b>=a and b>=c):
    print(b," is greatest")
elif(c>=a and c>=b):
    print(c," is greatest")