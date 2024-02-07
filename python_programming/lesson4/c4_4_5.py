"""関数内でグローバル変数に値を入れる"""
animal = 'cat'

def f():
    global animal
    animal = 'dog'
    print('local:', animal)

f()
print('global:', animal)