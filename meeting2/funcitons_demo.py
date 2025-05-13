# 2025-01-28
d = "2025-01-28"
#
month = 6
# month()
# print(type(print))

# print()
# month = get_month(d)
# my_var = 5
# def get_month(date_str):
#     print("inside get_month")
#     y, m, d = date_str.split("-")
#     month = int(m)
#     return month
#
# m = get_month("2000-12-12")
# print(m)

#
# a = get_month("2025-01-07")
# a = get_month("2025-03-07")
# print(my_var)
# # print(get_month("2025-01-07"))
# # a = print("b")
#
# # print(m)
#
# # print(get_month)
#
# user_date = input("Insert date")
# # t = get_month(user_date)
# m, d = get_month(user_date)
# # print(f"Your month: {m}")
#

def get_part_of_date(date_str, part="y"):
    print("inside get_part_of_date")
    y, m, d = date_str.split("-")
    match part.lower():
        case "y":
            return int(y)
        case "m":
            return int(m)
        case "d":
            return int(d)
# print(get_part_of_date("2000-12-12", "m"))

get_part_of_date(date_str="2000-12-12", part="m")
get_part_of_date(part="m", date_str="2000-12-12")
get_part_of_date("2000-12-12", part="m")
# get_part_of_date(part="m", "2000-12-12")



# print(get_part_of_date("2025-01-01"))
# print(get_part_of_date(
#     date_str="2025-01-01",
#     part="d"
# ))
# result = get_part_of_date(
#     part="d",
#     date_str="2025-01-01",
# )
# continue you work with result (d)

# print("a", "sdfsdf", "sdfsdf")

def foo(a, b, *nums):
    print("a", a)
    print("b", b)
    print("nums", nums)

# foo(4, 5, 6, 7, 8,9,10)

print("hi", "bye", "apple", sep="*", end="---------")
print("hi", "bye", "apple", sep="*")



#
# def bar(a, b, nums):
#     print("a", a)
#     print("b", b)
#     print("nums", nums)
#
# foo(1,2, 3, 4,5 ,6,7,8)
# bar(1,2,[3,4,5,6,7,8])
# foo(1,2, *range(3,9))

# print()