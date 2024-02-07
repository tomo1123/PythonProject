"""関数内でグローバル変数に値を入れる"""
animal = 'cat'

def f():
    animal = 'dog'
    print('after:', animal)

f()
print('global:', animal)