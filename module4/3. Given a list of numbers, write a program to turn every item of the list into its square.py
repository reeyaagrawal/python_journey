def list_sq(numbers) :
    new_list=[]
    for i in range (len(numbers)) :
        numbers[i]=numbers[i]**2
        new_list.append(numbers[i])
    return new_list

num=[10,20,30,40,50]
print(type(num))
print(list_sq(num))