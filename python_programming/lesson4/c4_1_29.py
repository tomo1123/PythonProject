"""タプルの引数をタプル化する"""
def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

t = ('Mike', 'Nancy')
say_something('Hi!', *t)

