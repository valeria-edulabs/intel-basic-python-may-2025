# name = input("Name: ")
# is_lower = input("Lower (l/u): ")
#
# while is_lower not in "lu":
#     is_lower = input("Incorrect try again (l/u): ")
#
# print(name.lower() if is_lower == "l" else name.upper())


# name = input("Name: ")
# while True:
#     is_lower = input("Insert (l/u): ")
#     if is_lower == "l" or is_lower == 'u':
#         break
#
# print(name.lower() if is_lower == "l" else name.upper())

# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1
#     # counter = counter + 1
# print("done")

# num = 5
grades = []
# grades = list()
while True:
    grade = input("Insert grade: ")
    if grade != '$':
        grades.append(int(grade))
    else:
        break
print(f"You max grade: {max(grades)}")
print(f"You min grade: {min(grades)}")
print(f"You avg grade: {sum(grades) / len(grades)}")