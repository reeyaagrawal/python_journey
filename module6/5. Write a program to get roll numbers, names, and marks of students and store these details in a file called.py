def data():
    roll=input("Enter roll no: ")
    name=input("Enter name: ")
    mark=input("Enter marks: ")
    return roll,name,mark

file=open("Marks.txt","w+")
while True:
    n=int(input("Press 1 if you want ot add more data : "))
    if n==1 :
        rollno,names,marks=data()
        file.writelines("Roll no : "+rollno) 
        file.writelines(" Name : "+names) 
        file.writelines(" Marks : "+marks) 
        file.writelines("\n")
    else:
        print("Entries written to file successfully!")
        break

file.close()