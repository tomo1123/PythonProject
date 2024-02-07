"""zipファイルを作成"""
import zipfile
import glob

with zipfile.ZipFile('test.zip', 'w') as z:
    for f in glob.glob('test_dir/**', recursive=True):
        print(f)
        z.write(f)