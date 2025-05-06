# Write a code that receives a 4-digits number
# and prints out the leftmost and the rightmost digit of the number.
num = int(input("Inset number: "))
print(num // 1000)
print(num % 10)