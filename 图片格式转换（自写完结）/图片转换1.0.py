"""
图片格式：jpg;png;gif;tif
要求：输入照片，选择转换格式，输出照片
"""
import time
import os
from PIL import Image

def main():
    while True:
        def canton():
            os.system('cls')
            print('|-------------Waiting--------------|') 
            print('|', end = '')
            for _ in range(17):
                print('->', end = '')
                time.sleep(0.1)
            print('|')
            os.system('cls')
            print('|----------------------------------|')
            print('|-------------Finished-------------|')
            print('|----------------------------------|')

        def transfer(filename, filename_transferred):
            img = Image.open(filename)
            canton()
            img.save(filename_transferred)
        
        choice = [['.jpg','.png','.gif','.tif'],
                  ['.jpg','.png','.gif','.tif'],
                  ['.jpg','.png','.gif','.tif'],
                  ['.jpg','.png','.gif','.tif']]

        index1 = int(input('源文件格式选择【1.JEPG;2.PNG;3.GIF;4.TIF】 >>> ')) - 1 # 源文件后缀choice[index1][index1]
        input_filename = input('输入源图片名 >>>')
        index2 = int(input('目标格式选择【1.JEPG;2.PNG;3.GIF;4.TIF】 >>> ')) - 1 # 源文件后缀choice[index1][index2]
        old_file = '%s%s' % (input_filename, choice[index1][index1])

        rename_choice = input('是否保留源文件名称(y/n)？ >>> ')
        if rename_choice == 'y':
            new_file = '%s%s' % (input_filename, choice[index1][index2])
        elif rename_choice == 'n':
            new_file_name = input('请输入名称 >>> ')
            new_file = '%s%s' % (new_file_name, choice[index1][index2])

        transfer(old_file, new_file)
        
        go = input('点击回车继续,其余任意键退出 >>> ')
        if go == '':
            pass
        else:
            break

if __name__ == '__main__':
    main()



