"""処理終了後に消去される一時ディレクトリを作成"""
import tempfile

with tempfile.TemporaryDirectory() as td:
    print(td)