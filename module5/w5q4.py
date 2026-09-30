def combine_list(a,b):
    new_list=[]
    for i in range(len(a)):
        if a[i]%2!=0 :
            new_list.append(a[i])

    for j in range(len(b)):
            if b[j]%2==0 :
                new_list.append(b[j])
    return new_list

list1=[11,12,13,14,15]
list2=[16,17,18,19,20]
print(combine_list(list1,list2))