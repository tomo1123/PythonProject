"""時間の計算"""
import datetime

now = datetime.datetime.now()
print(now)
d = datetime.timedelta(days=365)
print(now - d)