import random
upperChar="ABCDEFGHIJKLMNOPPQRSTUVWXYZ"
lowerChar="abcdefghijklmnopqrstuvwxyz"
special_char="!@#/$%"
digits="0123456789"
all_char=upperChar+lowerChar+special_char+digits
password=[]
for i in range(2):
    password.append(random.choice(upperChar))

password.append(random.choice(special_char))
password.append(random.choice(digits))
for i in range(6) :
    password.append(random.choice(all_char))

random.shuffle(password)

print("Your Passowrd is:",''.join(password))
