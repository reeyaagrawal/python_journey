a=input("Enter number : ")
original=int(a)
a=int(a)

if a<0 :  
    a=-a
    
rev=0

while a>0 :
    rev=(rev*10)+(a%10)
    a=a//10

if abs(original)==rev:
    print("Entered number is palindrome")
else : 
    print("Entered number is not palindrome")