f1 = open("w7q6_text1.txt", "r")
f2 = open("w7q6_text2.txt", "r")

lines1 = f1.readlines()
lines2 = f2.readlines()

middle = len(lines1) // 2

temp = lines1[middle]

lines1[middle] = lines2[-1] + "\n"

lines2[-1] = temp

f1.close()
f2.close()

f1 = open("w7q6_text1.txt", "w")
f2 = open("w7q6_text2.txt", "w")

f1.writelines(lines1)
f2.writelines(lines2)

f1.close()
f2.close()
print("Content swapped successfully!")