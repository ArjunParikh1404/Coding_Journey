# Sort students by marks in descending order using Bubble Sort.
# Time Complexity = O(n²), Space Complexity = O(1)

students = []
n = int(input("Enter number of students : "))

for i in range(n):
    name = input("Enter student name : ")
    marks = int(input("Enter marks : "))
    students.append([name, marks])

for i in range(len(students)):
    for j in range(len(students) - 1):
        if students[j][1] < students[j + 1][1]:
            students[j], students[j + 1] = students[j + 1], students[j]

for student in students:
    print(student[0], student[1])
