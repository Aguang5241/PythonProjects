# argparse 库是用来管理命令行参数输入的 
# 使用 argparse 处理命令行参数，目标是获取输入的图片路径、输出字符画的宽和高以及输出文件的路径

# -*- coding=utf-8 -*-
from PIL import Image
import argparse 

# 构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件，输出文件，输出字符画高和宽
parser.add_argument('file') # 输入文件
parser.add_argument('-o', '--output') # 输出文件
parser.add_argument('--width', type = int, default = 80) # 输出字符画宽
parser.add_argument('--height', type = int, default = 80) # 输出字符画高

args = parser.parse_args() # 解析获取参数

IMG = args.file # 输出图片文件路径
WIDTH = args.width # 输出字符画宽度
HEIGHT = args.height # 输出字符画高度
OUTPUT = args.output # 输出字符画路径

# 字符画是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（为了简化可以这么理解），字符的种类越多，
# 可以表现的颜色也越多，图片也会更有层次感。问题来了，我们是要转换一张彩色的图片，这么多的颜色，要怎么对应到单色的字符画上去？
# 这里就要介绍灰度值的概念了。
# 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像。
# 另外一个概念是 RGB 色彩：RGB色彩模式是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的
# 叠加来得到各式各样的颜色的，RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。
# 来自百度百科介绍我们可以使用灰度值公式将像素的 RGB 值映射到灰度值
# （注意这个公式并不是一个真实的算法，而是简化的 sRGB IEC61966-2.1 公式，真实的公式更复杂一些，不过在我们的这个应用场景下并没有必要）：
# gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

ascii_char = list(r"""`~!@#$%^&*()-=_+[]\{}|;':",./<>?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz""") # len(ascii_char) = 84

def get_char(r, b, g, alpha = 256): # RGB 值转字符的函数
    
    # 判断alpha值
    if alpha == 0: 
        return ' '
    
    # 获取字符串长度
    length = len(ascii_char)

    #将RBG的值转换，灰度值的范围0-255 但是字符集有84，需要后续转换
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    
    # 返回灰度值对应的字符
    return ascii_char[int(gray / unit)]

# 图片的处理步骤如下：
# 1.首先使用 PIL 的 Image.open 打开图片文件，获得对象 im
# 2.使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度，注意这个函数第二个参数使用 Image.NEAREST，表示输出低质量的图片。
# 3.遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符
# 4.将所有的像素对应的字符拼接在一起成为一个字符串 txt
# 5.打印输出字符串 txt
# 6.如果执行时配置了输出文件，将打开文件将 txt 输出到文件，如果没有，则默认输出到 output.txt 文件

# 图片处理步骤放入到 如下代码块中（表示如果 test1.py 被当作 python 模块 import 的时候，这部分代码不会被执行） 
if __name__ == '__main__': # 装逼写法
    
    # 打开图片并调整高和宽
    im = Image.open(IMG) 
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST) 

    # 初始化字符串
    txt = ''

    # 纵向扫描
    for i in range(HEIGHT):
        # 横向扫描
        for j in range(WIDTH):
            # 将(j, i)坐标的RGB图片转换为字符后添加到txt字符串
            txt += get_char(*im.getpixel((j, i)))
        # 换行
        txt += '\n'
    # 输出
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open(OUTPUT.txt, 'w') as f:
            f.write(txt)