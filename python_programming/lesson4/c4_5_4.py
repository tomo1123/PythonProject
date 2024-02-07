"""エラーの内容を表示"""
l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))