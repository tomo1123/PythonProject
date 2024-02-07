"""zipファイルを展開"""
import zipfile

with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')