# SGPA Calculator for DBATU University

import datetime
n = int(input("Enter the number of subjects: "))

subjects = {}
marks = []

# Input subject names and credits
for i in range(n):
    sub = input(f"\nEnter Subject Name {i+1}: ")
    credit = int(input(f"Enter Credit of {sub}: "))
    subjects[sub] = credit

# Input marks
for subject in subjects:
    mark = int(input(f"Enter marks in {subject}: "))
    marks.append(mark)

total = 0
fail = False

print("\n", " RESULT ".center(30, "="))

# Grade Calculation
for (subject, credit), mark in zip(subjects.items(), marks):

    if 91 <= mark <= 100:
        gp = 10
        grade = "EX"

    elif 86 <= mark <= 90:
        gp = 9
        grade = "AA"

    elif 81 <= mark <= 85:
        gp = 8.5
        grade = "AB"

    elif 76 <= mark <= 80:
        gp = 8
        grade = "BB"

    elif 71 <= mark <= 75:
        gp = 7.5
        grade = "BC"

    elif 66 <= mark <= 70:
        gp = 7
        grade = "CC"

    elif 61 <= mark <= 65:
        gp = 6.5
        grade = "CD"

    elif 56 <= mark <= 60:
        gp = 6
        grade = "DD"

    elif 51 <= mark <= 55:
        gp = 5.5
        grade = "DE"

    elif 40 <= mark <= 50:
        gp = 5
        grade = "EE"

    else:
        gp = 0
        grade = "FF"
        fail = True

    total += credit * gp

    print(f"\nSubject : {subject}")
    print(f"Marks   : {mark}")
    print(f"Grade   : {grade}")
    print(f"GP      : {gp}")

# SGPA Calculation
sgpa = total / sum(subjects.values())

print("\n",''.center(30, "="))
print(f"SGPA : {round(sgpa, 2)}")

# Final Result
if fail:
    print("Result : FAIL")
else:
    print("Result : PASS")


# Done this program by : Harshad Dhuppe on 07-06-2026 12:34 PM
print("\n", " THANK YOU ".center(30, "="))
print("Program executed on:", datetime.datetime.now().strftime("%d-%m-%Y at %H:%M:%S"))