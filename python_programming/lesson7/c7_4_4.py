"""処理終了後も残る一時ディレクトリを作成"""
import tempfile

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)