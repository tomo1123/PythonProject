"""ファイルを1行ずつ読み込む"""
with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        print(line, end='')
        if not line:
            break