"""デフォルト引数に空のリストを使う"""
def sample_func(x, l=[]):
    l.append(x)
    return l

r = sample_func(100)
print(r)

r = sample_func(100)
print(r)