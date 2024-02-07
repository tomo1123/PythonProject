"""処理終了後に消去される一時ファイルを作成"""
import tempfile

with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())