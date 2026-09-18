a=input("Enter number : ")
a=int(a)
count=0
if a<0 :    a=-a
while a>0 : 
    a=a//10
    count=count+1
print("Total number of digits in entered number are : ",count)