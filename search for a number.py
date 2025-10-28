#//search for a number x in this  tuple using loop
list=(1,4,9,16,25,36,49,64,81,100);
print(type(list));
x=int(input("enter the number u want to search: "));
i=0
found=False;
while(i<=len(list)-1):
    if(x==list[i]):
        print("found")     
        found=True
        break
     i += 1
if not found:
    print("not found")
    