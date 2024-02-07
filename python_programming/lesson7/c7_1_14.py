"""seek"""
with open('test.txt', 'r') as f:
    f.seek(5)
    print(f.read(1))