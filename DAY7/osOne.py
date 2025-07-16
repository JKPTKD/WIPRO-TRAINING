import os

#print(os.listdir('d:/wipro'))
print(f'Current directory: {os.getcwd()}')
newDir = 'daySeven'
if not os.path.exists(newDir):
    os.mkdir(newDir)

if os.path.exists(newDir):
    print(os.listdir(newDir))
    os.rename(os.path.join(newDir,'A'),os.path.join(newDir,'B')) #'daySeven/A'
    print(os.listdir(newDir))