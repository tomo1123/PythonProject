"""時間の表示"""
import datetime

now = datetime.datetime.now()
print(now.strftime('%d/%m/%y-%H%M%S%f'))