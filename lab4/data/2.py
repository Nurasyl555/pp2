import datetime
today = datetime.datetime.now()
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
print(tomorrow.strftime("%d"))
print(today.strftime("%Y-%m-%d"))
print(yesterday.strftime("%d"))