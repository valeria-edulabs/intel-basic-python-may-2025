# grades = []
# grade = input("Insert grade: ")
# while grade != '$':
#     grades.append(grade)
#     grade = input("Insert grade: ")
# print(grades)
# print('bye')


grades = []
while True:
    grade = input("Insert grade: ")
    if grade == '$':
        break
    grades.append(grade)

print(grades)
print('bye')



