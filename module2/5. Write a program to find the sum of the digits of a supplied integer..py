n=int(input("Enter number : "))
original=n
sum=0
while (n>0) :
    sum=sum+(n%10)
    n=n//10

print("Sum of all digits of ",original," is : ",sum)