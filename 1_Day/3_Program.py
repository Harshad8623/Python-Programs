# Program to find student's grade and grade point

marks = float(input("Enter percentage of marks: "))

if 91 <= marks <= 100:
    grade = "EX"
    point = 10.0

elif 86 <= marks <= 90:
    grade = "AA"
    point = 9.0

elif 81 <= marks <= 85:
    grade = "AB"
    point = 8.5

elif 76 <= marks <= 80:
    grade = "BB"
    point = 8.0

elif 71 <= marks <= 75:
    grade = "BC"
    point = 7.5

elif 66 <= marks <= 70:
    grade = "CC"
    point = 7.0

elif 61 <= marks <= 65:
    grade = "CD"
    point = 6.5

elif 56 <= marks <= 60:
    grade = "DD"
    point = 6.0

elif 51 <= marks <= 55:
    grade = "DE"
    point = 5.5

elif 40 <= marks <= 50:
    grade = "EE"
    point = 5.0

elif 0 <= marks < 40:
    grade = "EF"
    point = 0.0

else:
    print("Invalid Marks")
    exit()

print("Letter Grade:", grade)
print("Grade Point:", point)




# method 2 : using a function to calculate grade and grade point
def calculate_grade(marks):
    if 91 <= marks <= 100:
        return "EX", 10.0
    elif 86 <= marks <= 90:
        return "AA", 9.0
    elif 81 <= marks <= 85:
        return "AB", 8.5
    elif 76 <= marks <= 80:
        return "BB", 8.0
    elif 71 <= marks <= 75:
        return "BC", 7.5
    elif 66 <= marks <= 70:
        return "CC", 7.0
    elif 61 <= marks <= 65:
        return "CD", 6.5
    elif 56 <= marks <= 60:
        return "DD", 6.0
    elif 51 <= marks <= 55:
        return "DE", 5.5
    elif 40 <= marks <= 50:
        return "EE", 5.0
    elif 0 <= marks < 40:
        return "EF", 0.0
    else:
        print("Invalid Marks")
        exit()
marks = float(input("Enter percentage of marks: "))
grade, point = calculate_grade(marks)
print("Letter Grade:", grade)
print("Grade Point:", point)


# method 3 : using a dictionary to store grade and grade point
grade_dict = {
    (91, 100): ("EX", 10.0),
    (86, 90): ("AA", 9.0),
    (81, 85): ("AB", 8.5),
    (76, 80): ("BB", 8.0),
    (71, 75): ("BC", 7.5),
    (66, 70): ("CC", 7.0),
    (61, 65): ("CD", 6.5),
    (56, 60): ("DD", 6.0),
    (51, 55): ("DE", 5.5),
    (40, 50): ("EE", 5.0),
    (0, 39): ("EF", 0.0)
}
marks = float(input("Enter percentage of marks: "))
for (lower, upper), (grade, point) in grade_dict.items():
    if lower <= marks <= upper:
        print("Letter Grade:", grade)
        print("Grade Point:", point)
        break



# method 4 : using a list of tuples to store grade and grade point
grade_list = [
    (91, 100, "EX", 10.0),
    (86, 90, "AA", 9.0),
    (81, 85, "AB", 8.5),
    (76, 80, "BB", 8.0),
    (71, 75, "BC", 7.5),
    (66, 70, "CC", 7.0),
    (61, 65, "CD", 6.5),
    (56, 60, "DD", 6.0),
    (51, 55, "DE", 5.5),
    (40, 50, "EE", 5.0),
    (0, 39, "EF", 0.0)
]
marks = float(input("Enter percentage of marks: "))
for lower, upper, grade, point in grade_list:
    if lower <= marks <= upper:
        print("Letter Grade:", grade)
        print("Grade Point:", point)
        break


# method 5 : using a while loop to allow multiple grade calculations until the user decides to exit
while True:
    marks = float(input("Enter percentage of marks (or -1 to exit): "))
    if marks == -1:
        print("Exiting the grade calculator. Goodbye!")
        break
    elif 0 <= marks <= 100:
        grade, point = calculate_grade(marks)
        print("Letter Grade:", grade)
        print("Grade Point:", point)
    else:
        print("Invalid Marks. Please enter a value between 0 and 100.")


# method 6 : using a class to represent a student and calculate grade and grade point
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = None
        self.point = None

    def calculate_grade(self):
        if 91 <= self.marks <= 100:
            self.grade = "EX"
            self.point = 10.0
        elif 86 <= self.marks <= 90:
            self.grade = "AA"
            self.point = 9.0
        elif 81 <= self.marks <= 85:
            self.grade = "AB"
            self.point = 8.5
        elif 76 <= self.marks <= 80:
            self.grade = "BB"
            self.point = 8.0
        elif 71 <= self.marks <= 75:
            self.grade = "BC"
            self.point = 7.5
        elif 66 <= self.marks <= 70:
            self.grade = "CC"
            self.point = 7.0
        elif 61 <= self.marks <= 65:
            self.grade = "CD"
            self.point = 6.5
        elif 56 <= self.marks <= 60:
            self.grade = "DD"
            self.point = 6.0
        elif 51 <= self.marks <= 55:
            self.grade = "DE"
            self.point = 5.5
        elif 40 <= self.marks <= 50:
            self.grade = "EE"
            self.point = 5.0
        elif 0 <= self.marks < 40:
            self.grade = "EF"
            self.point = 0.0
        else:
            print("Invalid Marks")
            exit()
name = input("Enter student's name: ")
marks = float(input("Enter percentage of marks: "))
student = Student(name, marks)
student.calculate_grade()
print("Student Name:", student.name)
print("Letter Grade:", student.grade)
print("Grade Point:", student.point)    



# method 7 : using a match case to calculate grade and grade point
marks = float(input("Enter percentage of marks: "))
match marks:
    case m if 91 <= m <= 100:
        grade = "EX"
        point = 10.0
    case m if 86 <= m <= 90:
        grade = "AA"
        point = 9.0
    case m if 81 <= m <= 85:
        grade = "AB"
        point = 8.5
    case m if 76 <= m <= 80:
        grade = "BB"
        point = 8.0
    case m if 71 <= m <= 75:
        grade = "BC"
        point = 7.5
    case m if 66 <= m <= 70:
        grade = "CC"
        point = 7.0
    case m if 61 <= m <= 65:
        grade = "CD"
        point = 6.5
    case m if 56 <= m <= 60:
        grade = "DD"
        point = 6.0
    case m if 51 <= m <= 55:
        grade = "DE"
        point = 5.5
    case m if 40 <= m <= 50:
        grade = "EE"
        point = 5.0
    case m if 0 <= m < 40:
        grade = "EF"
        point = 0.0
    case _:
        print("Invalid Marks")
        exit()
print("Letter Grade:", grade)
print("Grade Point:", point)