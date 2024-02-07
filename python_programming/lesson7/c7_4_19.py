"""時間の計算"""
import datetime

now = datetime.datetime.now()
print(now)
d = datetime.timedelta(weeks=-1)
print(now + d)