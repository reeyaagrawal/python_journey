#Grade students based on marks
#marks >= 90, grade =“A”
#90 > marks >= 80, grade =“B”
#80 > marks >= 70, grade =“C”
#70 > marks, grade =“D”
marks=int(input("enter marks: "))
if(marks>=90):
    print("garde='A'")
elif(marks>=80 and marks<90):
    print("garde='B'")
elif(marks>=70 and marks<80):
    print("garde='C'")
elif(marks<70 and marks>0):
    print("garde:'D'")
else:
    print("enter valid marks")