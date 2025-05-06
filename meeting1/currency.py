# is_hot_day = True
# print(is_hot_day)

# print(5 < 6)
# print(10 == 6)
# print(10 != 6)
# print(2<=2)
#
# hot_day = True
# is_sunny = True
# is_raining = False
#
# print(is_sunny and is_raining)
# print(is_sunny or is_raining)
# print(not hot_day)


ils = float(input("Insert sum in ILS: "))
usd_rate = 3.7
euro_rate = 4.1

currency = input("Insert currency (usd, euro): ")
if currency == 'usd':
    if ils % 10 == 0 and ils > 1000:
        print("You are lucky!")
        print(f"You are getting ${(ils / usd_rate)*1.1} ")
    else:
        print(f"You are getting ${ils / usd_rate} ")
elif currency == "euro":
    print(f"You are getting {ils / euro_rate} Euros")
else:
    print("I don't know")
