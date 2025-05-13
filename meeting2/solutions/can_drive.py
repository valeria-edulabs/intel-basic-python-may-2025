# Exercise:

# Write a program that receives two arguments from the user:
# - drink (a string representing the alcoholic drink - one of: "beer", "wine", "whiskey", "water")
# and
# - amount (an integer representing the amount of drink consumed in milliliters)
# The program should print "You are allowed to drive" if it is legally allowed to drive,
# and "You are NOT allowed to drive" if you cannot drive based on the following legal limits:
#
# Beer: 500 ml (1 regular portion)
# Wine: 200 ml (1 regular portion)
# Whiskey: 50 ml (1 regular portion)

# If the amount consumed exceeds the legal portion for that drink type, you are not allowed to drive.
# If the amount consumed is within the legal limit, you are allowed to drive.
# If no alcohol was consumed (drink == "water"), you are allowed to drive.


drink = input("Insert drink (beer, wine, whiskey, water): ")
amount_ml = int(input("Insert amount in ml: "))

# Normalize the drink input to lowercase for case-insensitive comparison
drink = drink.lower()

# Define legal limits for each drink type
if drink == "beer":
    legal_limit = 500  # 500 ml for beer
elif drink == "wine":
    legal_limit = 200  # 200 ml for wine
elif drink == "whiskey":
    legal_limit = 50  # 50 ml for whiskey
elif drink == "water":
    print("You are allowed to drive")
    exit()
else:
    print("You are NOT allowed to drive")
    exit()

# Check if the amount consumed is within the legal limit
if amount_ml <= legal_limit:
    print("You are allowed to drive")
else:
    print("You are NOT allowed to drive")