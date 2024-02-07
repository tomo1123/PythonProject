"""copyメソッドを試す"""
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)