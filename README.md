# CopyFile
Copy files under the specified folder according to the specified file type
根据输入的文件路径和文件后缀
遍历文件，并用正则匹配后缀名
再将匹配到的文件复制到指定文件夹下

引用库：os, os.path, shutil(用于复制文件), re(正则匹配), progress（打印进度条）
