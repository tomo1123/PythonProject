"""パイプラインの実行"""
import subprocess

subprocess.run('ls -al | grep test', shell=True)