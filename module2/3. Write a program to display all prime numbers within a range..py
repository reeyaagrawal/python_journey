n=input("Enter range start ")
m=input("Enter range end ")
n=int(n)
m=int(m)
for i in range(n,m+1) :
    if i<2 :
        continue
    for j in range (2,i) :
        if i%j==0:
            break
    else :
        print(i)        