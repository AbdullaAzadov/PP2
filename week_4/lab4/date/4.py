import datetime

date = datetime.datetime.strptime('2023-02-28 01:59:59', '%Y-%m-%d %H:%M:%S')
current = datetime.datetime.now()
difference = current - date

print((difference.days * 24 * 3600) + difference.seconds ,"seconds")