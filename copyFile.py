import os
import os.path
import shutil
import re
from progress.bar import Bar

# 用于存放后缀名匹配的文件
greplist = []

def printdir(path, depth, pattern):
    '''
    遍历输出目录文件同时匹配后缀名
    '''
    for item in os.listdir(path):
        print("|      " * depth + item)
        # 匹配文件后缀文件名
        match = pattern.match(item)
        if match:
            greplist.append(path + '/' + item)
        newitem = path + '/' + item
        if os.path.isdir(newitem):
            printdir(newitem, depth + 1, pattern)

def copy_file(greplist, suffix = "copy"):
    '''
    复制抓取匹配到的文件
    '''
    if 0 == len(greplist):
        print("No Match File!")
        return

    # 目标文件夹
    copytodir = os.path.curdir + '/' + suffix
    if not os.path.exists(copytodir):
        os.mkdir(copytodir)
    os.chdir(copytodir)

    # 打印进度条 
    length = len(greplist)
    bar = Bar('Copying...', max = length)

    for item in greplist:
        # 复制匹配到的文件
        try:
            # 当前目录文件不复制
            if item.startswith('.'):
                print("File %s is existed!" % item)
            else:
                shutil.copy(item, os.path.curdir)
        except PermissionError:
            # 没有复制权限
            print("Don't have permission to copy the file ", item)
        except FileNotFoundError:
            # 找不到文件
            print("Can't found file ", item)  
        bar.next()
    bar.finish()

if __name__ == '__main__':
    path = input("Enter path:\n")
    if path == "":
        path = "."
    suffix = input("Enter suffix(eg: txt):\n")
    pattern = re.compile(".*\."+suffix+"$")
    print("Directory scan of ", path)
    printdir(path, 0, pattern)
    copy_file(greplist, suffix)
