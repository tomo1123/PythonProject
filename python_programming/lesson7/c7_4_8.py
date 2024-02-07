"""shell=Trueを用いたコマンドの実行"""
import subprocess

subprocess.run('ls -al', shell=True)