import sys
import os


'''
创建init.py文件
'''
def create():

    newfile = "__init__.py"

    if not os.path.exists(newfile):
        f = open(newfile,'w')
        f.close()

    else:
        print(newfile + " already existed.")


def delete_file():
    '''删除所有大小为0的文件'''
    directory = "./testreport"

    files = os.listdir(os.getcwd())
    #print(os.getcwd())  #C:\Users\Administrator\Desktop\seleniumUI\public\common
    #files = os.listdir(os.chdir(directory))
    for file in files:
        if os.path.getsize(file) == 0:  # 获取文件大小
            os.remove(file)
            print(file + " deleted.")


#create()
delete_file()



