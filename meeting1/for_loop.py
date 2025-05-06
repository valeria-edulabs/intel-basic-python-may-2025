names = []
grades = []

count = int(input("Insert number of grades: "))

for i in range(count):
    name, grade = input("Insert name and grade: ").split()
    grade = int(grade)
    names.append(name)
    grades.append(grade)

print(names, grades)
avg = sum(grades) / len(grades)
print(avg)

# print(10*i)
print("bye")