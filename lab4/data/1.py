import datetime
correct_time = datetime.datetime.now()
minus_5days = correct_time - datetime.timedelta(days=5)
minus_1 = correct_time - datetime.timedelta(weeks=5)
print(minus_5days)
print(minus_1.strftime("%x"))