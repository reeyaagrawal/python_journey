def calc_sum_sub(a,b) :
    return a+b,a-b

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
sum,sub=calc_sum_sub(num1,num2)
print("Sum of",num1,"and",num2,"is:",sum)
print("Difference of",num1,"and",num2,"is:",sub)