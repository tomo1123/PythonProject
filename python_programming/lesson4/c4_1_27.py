"""位置引数のタプル化"""
def say_something(*args):
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nancy')