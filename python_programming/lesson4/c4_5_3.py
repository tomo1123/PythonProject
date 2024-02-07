"""特定のエラーの処理"""
l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError:
    print("Don't worry")