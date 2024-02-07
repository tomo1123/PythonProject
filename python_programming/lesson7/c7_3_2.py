"""tarファイルを展開"""
import tarfile

with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall('test_tar')