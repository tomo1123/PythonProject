"""特定のエラーの処理"""
l = [1, 2, 3]
i = 5
del l
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)