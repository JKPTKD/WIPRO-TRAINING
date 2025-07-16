import os
import datetime

def listDir(path="."):
    return os.listdir(path)

def getCWD():
    return os.getcwd()

def date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
