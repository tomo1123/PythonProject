"""任意の時刻の表示"""
import datetime

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H%M%S%f'))