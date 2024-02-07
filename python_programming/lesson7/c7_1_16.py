"""'w'でopenしたファイルを読み込む"""
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w') as f:
    f.write(s)
    print(f.read())