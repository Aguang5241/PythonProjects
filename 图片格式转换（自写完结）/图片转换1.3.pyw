import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from PIL import Image

def main():   
    window1 = tk.Tk()
    window1.title('')
    window1.geometry('200x100')

    l1 = tk.Label(window1, bg = 'green', font = ('宋体', 12), width = 50, text = '图片转换精灵（v1.3）')
    l1.pack()

    def select_image():
        image = tk.filedialog.askopenfilenames(title = '选择图片')
        num = len(image)
        types = ['.jpg', '.png', '.tif', '.gif']
        image_list = list(image)
        
        window2 = tk.Tk()
        window2.title('')
        window2.geometry('200x250')
        
        l2_1 = tk.Label(window2, bg = 'green', font = ('宋体', 12), width = 50, text = '图片转换精灵（v1.3）')
        l2_1.pack()

        l2_2 = tk.Label(window2, text = '')
        l2_2.pack()
        
        l2_3 = tk.Label(window2, font = ('宋体', 12), width = 50, text = '')
        l2_3.pack()
        l2_3.config(text = '已选择%d张图片' % num)
        
        l2_4 = tk.Label(window2, font = ('宋体', 12), width = 50, text = '目标格式【点击即开始】')
        l2_4.pack()

        l2_5 = tk.Label(window2, text = '')
        l2_5.pack()


        def jpg_type():
            image_type = types[0]
            for img in image_list:
                f = Image.open(img)
                img_name = img[:-4]
                try:
                    f.save(img_name + image_type)
                except OSError:
                    tkinter.messagebox.showerror(title='', message='%s转换出错' % img)

            tkinter.messagebox.showinfo(title='', message='转换完成')       

        def png_type():
            image_type = types[1]
            for img in image_list:
                f = Image.open(img)
                img_name = img[:-4]
                try:
                    f.save(img_name + image_type)
                except OSError:
                    tkinter.messagebox.showerror(title='', message='%s转换出错' % img)

            tkinter.messagebox.showinfo(title='', message='转换完成')       

        def tif_type():
            image_type = types[2]
            for img in image_list:
                f = Image.open(img)
                img_name = img[:-4]
                try:
                    f.save(img_name + image_type)
                except OSError:
                    tkinter.messagebox.showerror(title='', message='%s转换出错' % img)
                
            tkinter.messagebox.showinfo(title='', message='转换完成')       

        def gif_type():
            image_type = types[3]
            for img in image_list:
                f = Image.open(img)
                img_name = img[:-4]
                try:
                    f.save(img_name + image_type)
                except OSError:
                    tkinter.messagebox.showerror(title='', message='%s转换出错' % img)

            tkinter.messagebox.showinfo(title='', message='转换完成')       

        button2_1 = tk.Button(window2, text = 'JEPG', font = ('宋体', 12), width = 8, height = 1, command = jpg_type)
        button2_1.pack()
        button2_2 = tk.Button(window2, text = 'PNG', font = ('宋体', 12), width = 8, height = 1, command = png_type)
        button2_2.pack()
        button2_3 = tk.Button(window2, text = 'TIF', font = ('宋体', 12), width = 8, height = 1, command = tif_type)
        button2_3.pack()
        button2_4 = tk.Button(window2, text = 'GIF', font = ('宋体', 12), width = 8, height = 1, command = gif_type)
        button2_4.pack()
        
        window2.mainloop()
               
    botton1 = tk.Button(window1, text = '选择图片', font = ('宋体', 12), width = 8, height = 1, command = select_image)
    botton1.place(x = 65, y = 40)

    window1.mainloop()

if __name__ == '__main__':
    main()