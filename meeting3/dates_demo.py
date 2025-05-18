import datetime

now = datetime.datetime.now()
print(now)
print(type(now))


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

dt = datetime.datetime(1987, 2, 11)
print(type(dt))
print(days[dt.weekday()])

#https://strftime.org/
parsed_date = datetime.datetime.strptime(
    "2024-02-08, hours: 15:09",
    "%Y-%m-%d, hours: %H:%M")
print(parsed_date)
print(type(parsed_date))

print(now)
formatted_date = now.strftime("%d/%m/%Y, %A")
print(type(formatted_date), formatted_date)

# dd/mm/yyyy, Tue

# 1/2/2024
# 2024-02-01

bday = datetime.datetime.strptime(
    '11-02-2025', '%d-%m-%Y')
diff = bday - datetime.datetime.now()
print(diff, type(diff))

print(diff.total_seconds())
print("hours left:", diff.total_seconds() / 3600)

diff2 = datetime.datetime.now() - \
        datetime.datetime(1987, 2, 11)

print(diff2)

print(bday < datetime.datetime.now())

print(diff2.days+100)

#01/02/24

ts = 1738669626
print(datetime.datetime.fromtimestamp(ts))