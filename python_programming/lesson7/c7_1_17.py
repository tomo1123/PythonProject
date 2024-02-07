"""'w+'でopen"""
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w+') as f:
    f.write(s)
    print(f.read())