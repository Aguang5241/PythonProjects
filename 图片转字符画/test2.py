#coding:utf-8
from PIL import Image
import argparse 

parser = argparse.ArgumentParser()

parser.add_argument('file') 
parser.add_argument('-o', '--output')
parser.add_argument('--width', type = int, default = 100) 
parser.add_argument('--height', type = int, default = 100) 

args = parser.parse_args() 

IMG = args.file 
WIDTH = args.width 
HEIGHT = args.height 
OUTPUT = args.output 

ascii_char = list(r"""0123456789$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. """)

def get_char(r, b, g, alpha = 256): 
    
    if alpha == 0: 
        return ' '
    
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]
    


if __name__ == '__main__':
    
    rgb_im = Image.open(IMG)
    im = rgb_im.convert('RGB') 
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST) 
    # 第二个参数resample有四个选项，分别是Image.NEAREST、Image.BILINEAR、Image.BICUBIC、Image.LANCZOS
    # 默认是第一个，第四个质量最高

    txt = ''

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i))) # getpixel()方法会返回四个元素的元组
        txt += '\n'
    print(txt)
       
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)

    
    
    

    
            
 
 
 
 
 
 
 

 
    
    
        
   
    
   
