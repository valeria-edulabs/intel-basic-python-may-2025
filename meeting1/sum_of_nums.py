#Write a program that receives a number from a user
# and calculates the sum of all numbers from 1 to a given number

# Option 1
num = int(input("Insert number: "))
total = 0
for i in range(num+1):
    total += i

print(f"The total is: {total}")

# Option 2
num = int(input("Insert number: "))
all_nums = []
for i in range(num+1):
    all_nums.append(i)
print(f"The total is: {sum(all_nums)}")
