"""ファイルの現在位置を確認する"""
with open('test.txt', 'r') as f:
    print(f.tell())