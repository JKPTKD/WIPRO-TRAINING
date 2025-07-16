import os
import shutil

def makeDir(path):
    os.makedirs(path, exist_ok=True)

def rmDir(path):
    shutil.rmtree(path)

def chDir(path):
    os.chdir(path)
