


print("===== Student Grade Calculator =====")


name = input("Enter student name: ")


subjects = ["Cloud Computing", "Maths", "Python", "DBMS", "AI"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks in {subject} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

total = sum(marks)
percentage = total / len(subjects)


if any(mark < 35 for mark in marks):
    result = "Fail"
    grade = "F"
elif percentage >= 90:
    result = "Pass"
    grade = "A+"
elif percentage >= 80:
    result = "Pass"
    grade = "A"
elif percentage >= 70:
    result = "Pass"
    grade = "B"
elif percentage >= 60:
    result = "Pass"
    grade = "C"
elif percentage >= 50:
    result = "Pass"
    grade = "D"
else:
    result = "Pass"
    grade = "E"


print("\n===== Student Result =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
print("Result:", result)

print("==========================")
