import datetime


# datetime.datetime
# datetime.date
# datetime.time
# datetime.timedelta

now = datetime.datetime.now()
print(now)
print(type(now))

print(now.weekday())

#
days = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
    4: "Fri",
    5: "Sat",
    6:" Sun"
}
print(days[now.weekday()])
print(now.month, now.second)

bday = datetime.datetime(2026,2,11)
print(bday)
print(bday - now)
print(bday < now)
# print(bday + now)
print(now + datetime.timedelta(10, hours=37))

"2025-12-30"
"2025-12-30T13:24:54.456"
d1 = "5/24/2004"
d2 = "2025-12-30"
# d1 < d2
date1 = datetime.datetime.strptime(d1, "%m/%d/%Y")
print(d1, date1)

in10days = now + datetime.timedelta(10, hours=37)
print(in10days)

print(in10days.strftime("%d/%m/%Y, %A"))

print(in10days.timestamp())

ts = 1747722130
print(datetime.datetime.fromtimestamp(ts))

#
# dt = datetime.datetime(1987, 2, 11)
# print(type(dt))
# print(days[dt.weekday()])
#
# #https://strftime.org/
# parsed_date = datetime.datetime.strptime(
#     "2024-02-08, hours: 15:09",
#     "%Y-%m-%d, hours: %H:%M")
# print(parsed_date)
# print(type(parsed_date))
#
# print(now)
# formatted_date = now.strftime("%d/%m/%Y, %A")
# print(type(formatted_date), formatted_date)
#
# # dd/mm/yyyy, Tue
#
# # 1/2/2024
# # 2024-02-01
#
# bday = datetime.datetime.strptime(
#     '11-02-2025', '%d-%m-%Y')
# diff = bday - datetime.datetime.now()
# print(diff, type(diff))
#
# print(diff.total_seconds())
# print("hours left:", diff.total_seconds() / 3600)
#
# diff2 = datetime.datetime.now() - \
#         datetime.datetime(1987, 2, 11)
#
# print(diff2)
#
# print(bday < datetime.datetime.now())
#
# print(diff2.days+100)
#
# #01/02/24
#
# ts = 1738669626
# print(datetime.datetime.fromtimestamp(ts))
#
