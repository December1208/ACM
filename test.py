import datetime
import time


start = datetime.datetime.now() - datetime.timedelta(days=30)
start = int(time.mktime(start.timetuple()))
end = int(time.time())
print(start, end)
