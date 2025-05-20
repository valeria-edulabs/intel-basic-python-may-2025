# open("/Users/valeria/Downloads/API - functions - Callable from UI.csv")
# path = "C:\\sdf\\sdf\\f"
import csv
import datetime
import pprint

WEEKDAYS = {
    0: "Mon",
    1: "Tue",
    2: "Wed",
    3: "Thu",
    4: "Fri",
    5: "Sat",
    6:" Sun"
}

def get_weekly_averages(year: int):
    with open("../data/AAPL.csv", "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        weekday_dict: dict[str, list[float]] = {}
        for entry in reader:
            date = datetime.datetime.strptime(entry['Date'], "%d-%m-%Y")
            close_price = float(entry['Close'])
            if date.year == 2021:
                weekday_name = WEEKDAYS[date.weekday()]
                if weekday_name not in weekday_dict:
                    weekday_dict[weekday_name] = []
                weekday_dict[weekday_name].append(close_price)

    ret_dict = {}
    for weekday, prices in weekday_dict.items():
        ret_dict[weekday] = sum(prices) / len(prices)
    return ret_dict


pprint.pprint(get_weekly_averages(2021))
pprint.pprint(get_weekly_averages(2020))
pprint.pprint(get_weekly_averages(2019))

