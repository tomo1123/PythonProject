"""デフォルト引数に空のリストではなくNoneを使う"""
def sample_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = sample_func(100)
print(r)

r = sample_func(100)
print(r)