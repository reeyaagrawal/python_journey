employee = open("Employee.txt", "r")
department = open("Department.txt", "r")

salary = {}
count = {}

for line in employee:
    data = line.strip().split(",")

    name = data[0]
    eid = data[1]
    sal = int(data[2])
    did = data[3]

    salary[did] = salary.get(did, 0) + sal
    count[did] = count.get(did, 0) + 1

employee.close()

for line in department:
    data = line.strip().split(",")

    did = data[0]
    dname = data[1]

    if did in salary:
        average = salary[did] / count[did]
        print(dname, "=", average)

department.close()