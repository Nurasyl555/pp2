import datetime
x = datetime.datetime(2024, 1, 12, 12, 20)
y = datetime.datetime(2024, 1, 12, 12, 40)
z = abs(x - y).total_seconds()
print(z)