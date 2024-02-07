"""ファイルをチャンクごとに読み込む"""
with open('test.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break