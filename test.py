import os

cwd = os.getcwd()
path = "api/app.py"
newp =  os.path.join(cwd,path)

print('path is {0}'.format(newp))