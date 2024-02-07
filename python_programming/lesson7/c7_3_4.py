"""zipファイルを作成"""
import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('test_dir')
    z.write('test_dir/test.txt')