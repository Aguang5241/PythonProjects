#-*- coding:utf8 -*-

from PIL import Image

im = Image.open('captcha.gif')
# 将图像转换为8位像素模式
im.convert('P')

# 打印颜色直方图
# 颜色直方图的每一个数字都代表对应位置颜色的数量
# RBG格式共有256位（种）颜色，im.histogram()罗列出各个位（种）颜色的数量
his = im.histogram()
# 排序获得所需要的主要颜色
# 例图中我们主要需要红色220与灰色227
value = {}
for i in range(256):
    value[i] = his[i]
for j, k in sorted(value.items(), key = lambda x : x[1], reverse = True):
    print(j, k) 
    

    
