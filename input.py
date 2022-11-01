name = input("Please enter your name:")
age = int(input("Please enter your age: "))
weight = float(input("please enter your weight: "))
print('name: '+name)
print('age: '+str(age)+" years old")
print('weight: '+str(weight)+" kg")

# if
key=int(input("Press 1:"))
if key == 1:
    score = float(input("fill in the score:"))
    percent = score/35*100
    print("score %.1f \nthe percentage is %.1f%%" %(score, percent))
print("see you again!")

#if else
a = int(input("input a: "))
b = int(input("input b: "))
if a <b:
    print(a, "<", b)
else:
    temp = a
    a = b
    b = temp
    print(a, "and", b, "switched")
print(a, ",", b)

# if else elif
print("Menu")
print("1.Plus")
print("2.Minus")
print("3.Multiplied")
print("4.Divide")
key = int(input("slected press 1, 2, 3 or 4: "))
a = int(input("Enter numbers1: "))
b = int(input("Enter numbers2: "))
if key == 1:
    print("positive effect of", a, "+", b, "="(a+ b))
elif key == 2:
    print("negative effect of", a, "-", b, "=", (a-b))
elif key == 3:
    print("multiply result of", a, "*", b, "=", (a*b))
elif key == 4:
    print("quotient of", a, "/",b, "=",(a/b))
else:
    print("An error was encountered in selecting the operator!")
print("see you again!")

#while
count = 1
total = 0
while count <= 20:
    total += count
    count += 1
print("Sum from 1 to 20 =", total)

# for
N = int(input("number of students: "))
avg = 0
total = 0
for count in range(1, (N + 1)):
    score = float(input("test scores of the students" + str(count) + ":"))
    total += score
arg = total / N
print("point average =", avg)

print("Odd numbers from 1 to 20 consist of")
for count in range(1, 21, +2):
    print(count, end="")

# break
while True:
    ch = input("character input: ")
    if 'a' <= ch <= 'z':
        print(ch, "in english alphabet")
    elif 'A' <= ch <= 'Z':
        print(ch, "in english alphabet")
    else:
        print(ch, "not english letters")
    break

# pass
password = ["12345", "1111"]
pw = input("password is: ")
for data in password:
    if data != pw:
        pass
    else:
        print("Found this password.")
print("see you again")

#continue
count = 1
while count <= 5:
    score = float(input("test scores of the students" + str(count) + ":"))
    if score < 0 or score > 100:
        print("Incorrect score information")
        continue
    print("The score information is correct.")
    count += 1

# str
loginList = "87654321"
checkList = loginList[0:len(loginList):2]
check = False
while not check:
    password = input("enter your password: ")
    if password == checkList:
        print("Login successfully")
        break
    else:
        print("Incorrect password. Please try again.")

# function
def calwage():
    global total
    total=(40*r)+(h-40)*(1.5* r)
h = 50
r = 100
calwage()
print("the total working hours = {:,d} hours".format(h))
print("labor rate = {:,.2f} THB per hour".format(r))
print("the total amount of wages = {:,.2f} THB".format(total))

def calwage(hr,rate):
    global total
    total=(40*rate)+(hr-40)*(1.5* rate)
h = 50
r = 100
calwage(h, r)
print("the total working hours = {:,d} hours".format(h))
print("labor rate = {:,.2f} THB per hour".format(r))
print("the total amount of wages = {:,.2f} THB".format(total))

def calwage():
    global total
    total=(40*r)+(h-40)*(1.5* r)
    return total
h = 50
r = 100
result = calwage()
print("the total working hours = {:,d} hours".format(h))
print("labor rate = {:,.2f} THB per hour".format(r))
print("the total amount of wages = {:,.2f} THB".format(result))

def calwage(hr, rate):
    global total
    total=(40*rate)+(hr-40)*(1.5* rate)
    return total
h = 50
r = 100
result = calwage(h, r)
print("the total working hours = {:,d} hours".format(h))
print("labor rate = {:,.2f} THB per hour".format(r))
print("the total amount of wages = {:,.2f} THB".format(result))

# file
try:
    data1 = float(input("numeric data 1: "))
    data2 = float(input("numeric data 2: "))
    print("information is", data1, data2, end=" => ")
    print("The data type was converted successfully.")
except ValueError as e:
    print("The data type cannot be converted.")
    print("Value Error: ", e)

# list
key = 1
passList = ["236428", "339212", "326224", "818339", "111212"]
while (key > 0) and (key < 3):
    print("เมนูหลัก")
    print("1.View information about people who passed the exam.")
    print("2.Search results")
    key = int(input("Menu: "))
    if key == 1:
        print(passList)
    if key == 2:
        studentID = input("Enter the applicant number: ")
    if studentID in passList:
        idx = passList.index(studentID)
        print("You passed the exam in order of", idx + 1)
    else:
        print("you failed the exam see you next round")

# tuple
userList = ("admin;2468", "admin;7531")
uList = []
pList = []
for i in range(0, len(userList)):
    data = userList[i].split(";")
    uList.append(data[0])
    pList.append(data[1])
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    data = username + ";" + password
    if data in userList:
        print("login successfully")
        break
    else:
        if username in uList:
            print(" Incorrect password. Please try again. ")
        elif password in pList:
            print(" Username is incorrect. Please try again. ")
        else:
            print(" Your details are incorrect. Please try again. ") 

# dict
passList = {"236428": "scl", "339212": "nurse", "326224": "sc", "818339" :"engineer",
"111212":"nurse"}

facList = {"sci": "scientifically", "nurse": " nursing program", "engineer": "engineering"}
studentID = input("Enter the applicant number: ")
if studentID in passList:
    facCode = passList.get(studentID)
    print("you passed the exam", facList(facCode))
else:
    print("you failed the exam see you next round")

# set
total1 ={1,2.3,4,5,6, 7.8,9, 10}
math1 = {1, 3, 5, 6, 7,9}
eng1 = {1,3,5,8, 10}
print("those learning Math: ", math1, "=", len(math1))
print(" those learning English: ", eng1, "=", len(eng1))
print("those learning Math and English: ", math1.intersection(eng1), "=",
    len(math1.intersection(eng1)))
print("คนที่เรียนคณิตศาสตร์แต่ไม่เรียนภาษาอังกฤษ ได้แก่", math1.differencee(eng1),
"=", len(math1.difference(eng1)))
print("คนที่เรียนภายาอังกฤษแต่ไม่เรียนคณิตศาสตร์ ได้แก่", eng1.difference(math1),
"=", len(eng1.difference(math1)))
both = math1.union(eng1)
print("จำนวนคนที่เรียนกาษาอังกฤษเละคณิตศาสตร์ทั้งหมด", len(both), "คน ได้แก่", both)
print("คนที่ไม่เรียนทั้งสองวิชา ได้แก่", total.difference(both), "=", len(total1.
difference(both)))