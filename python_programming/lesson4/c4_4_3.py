"""関数内でグローバル変数に値を入れる"""
animal = 'cat'

def f():
    print(animal)
    animal = 'dog'
    print('after:', animal)

f()