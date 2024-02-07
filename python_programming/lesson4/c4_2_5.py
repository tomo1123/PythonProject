"""関数の実行前と実行後に処理を行う"""
def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)
print('end')

print(r)