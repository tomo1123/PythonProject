"""__name__や__doc__を出力する"""
animal = 'cat'

def f():
    """Test func doc"""
    print(f.__name__)
    print(f.__doc__)

f()
print('global:', __name__)
