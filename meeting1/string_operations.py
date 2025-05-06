word = "Weather"
print(word[0])
print(word[2])
print(word[-1])
print(word[-3])
print(word[2:4])
print(word[2:14])
print(word[2:-2])
# print(word[start:end:step])
print(word[2:4:-1])
print(word[4:2:-1])
print(word[5:1:-2])
print(word[-1:0:-1])
print(word[-1::-1])
print(word[::-1])

text = "The life is beautiful"
print(text + word)
print(text * 5)
# print(text + "5")
print(len(text))
print(text)

num = 10
text1 = text.lower()
print("text", text)
print("text1", text1)

print(text.count("i"))

words = text.split(" ")
print(words)

print(len(words))
print(words[-1])
print(len(words[-1]))

print(type(words))
words.append("hi")
print(words)

prices = [102, 103.4, 101.7]

names = []
grades = []
user_input = input("Insert name and grade separated by space: ")
name, grade = user_input.split()
grade = int(grade)
names.append(name)
grades.append(grade)

user_input = input("Insert name and grade separated by space: ")
name, grade = user_input.split()
grade = int(grade)
names.append(name)
grades.append(grade)
print(names, grades)

i = 0
print(names[i], grades[i])
i += 1
print(names[i], grades[i])