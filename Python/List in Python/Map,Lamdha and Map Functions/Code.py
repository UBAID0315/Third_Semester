from datetime import date

current_date = date.today()
items = ["Milk", "Bread", "Eggs", "Yogurt", "Cheese"]
expiration_dates = [date(2023, 10, 15), date(2023, 10, 15),
                    date(2023, 9, 25), date(2023, 9, 8), 
                    date(2023, 8, 10)]

filtered = list(filter(lambda value: value > current_date, expiration_dates))
zipped = zip(items,filtered)

print("Invntory of Unexpired items: ")
print(list(zipped))
