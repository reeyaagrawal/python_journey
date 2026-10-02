str=input("Enter string: ")
c_upper=0
c_lower=0
c_alpha=0
c_digit=0

for i in  range(len(str)) :
    if str[i].isalpha():
        c_alpha=c_alpha+1
    if str[i].islower():
        c_lower=c_lower+1
    if str[i].isupper():
        c_upper=c_upper+1
    if str[i].isdigit():
        c_digit=c_digit+1

print("Number of upper character : ",c_upper)
print("Number of lower character : ",c_lower)
print("Number of Alphabets : ",c_alpha)
print("Number of digits : ",c_digit)