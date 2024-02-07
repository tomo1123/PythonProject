"""型が宣言された関数の呼び出し"""
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num('a', 'b')
print(r)