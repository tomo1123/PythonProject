"""zipファイルの中身を確認"""
import zipfile

with zipfile.ZipFile('test.zip', 'r') as z:
    with z.open('test_dir/test.txt') as f:
        print(f.read())