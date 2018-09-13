#!/usr/bin/evn python3
#coding=utf-8
import shutil,os

# def parseArgument():
#     for i in range(0,len(sys.argv)):
#          print(sys.argv[i])
#          argu = sys.argv[i]
#     return argu

if __name__ == '__main__':
    ROOT = os.getcwd() #当前目录
    # ROOT_HEXO = ROOT + "/hexo/"
    ROOT_HEXO = ROOT
    NAME = ".git--"
    N_NAME = ".git"
    DIR = ROOT_HEXO + NAME

    if os.path.exists(DIR) == True:
        # print(ROOT_HEXO + NAME,"--------->")
        #重命名文件夹
        try:
            shutil.move(DIR,ROOT_HEXO + N_NAME)
        except Exception,e:  
            print Exception,":",e
    else:
        try:
            shutil.move(ROOT_HEXO + N_NAME,DIR)
        except Exception,e:  
            print Exception,":",e