"""'r+'でopen"""
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)