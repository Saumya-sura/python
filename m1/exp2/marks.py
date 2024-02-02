marks = []
subjects = int(input("Enter the number of subjects studying in this semester: "))

for i in range(subjects):
    mark = int(input(f"Enter the mark for subject {i+1}: "))
    if mark < 0 or mark > 100:
        print("Invalid mark. Mark should not be negative and should not be more than 100.")
        break
    marks.append(mark)#add an element to it

total = sum(marks)
percentage = (total / (subjects * 100)) * 100

if percentage >= 92:
    grade = "Merit"
elif percentage >= 75:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First class"
elif percentage >= 45:
    grade = "Second class"
else:
    grade = "Fail"

print(f"Total Marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
