import tkinter as tk
from tkinter import filedialog
from PIL import Image

def main():
    window1 = tk.Tk()
    window1.title('图片转换精灵（v1.2）')
    window1.geometry('400x300')
    l1 = tk.Label(window1, bg = 'green', font = ('宋体', 16), width = 30, text = '请选择')
    l1.place(x = 35, y = 100)

    def print_image_selection():
        global images
        images = tk.filedialog.askopenfilenames(title = '选择图片')
        num = len(images)
        l1.config(text = '已选择%d个图片' % num)

    def type_select():
        window2 = tk.Tk()
        window2.title('图片转换精灵（v1.2）')
        window2.geometry('400x300')
        
        var = tk.StringVar()
        l2 = tk.Label(window2, bg = 'green', width = 50, text = '请选择')
        l2.pack()
        
        
        def print_type_selection():
            global type_name
            type_name = var.get()
            l2.config(text='目标格式为:' + var.get())
        
        r1 = tk.Radiobutton(window2, text='JEPG', variable=var, value='.jpg', command=print_type_selection)
        r1.pack()
        r2 = tk.Radiobutton(window2, text='PNG', variable=var, value='.png', command=print_type_selection)
        r2.pack()
        r3 = tk.Radiobutton(window2, text='TIF', variable=var, value='.tif', command=print_type_selection)
        r3.pack()
        r4 = tk.Radiobutton(window2, text='GIF', variable=var, value='.gif', command=print_type_selection)
        r4.pack()

        window2.mainloop()
    
    def transfer():
        types = ['.jpg', '.png', '.tif', '.gif']
        for image in images:
            f = Image.open(image)
            name = image[:-4]
            f.save('%s%s' % (name, type_name))

    select_button1 = tk.Button(window1, text = '转换选项', font = ('宋体', 12), width = 8, height = 1, command = type_select)
    select_button1.place(x = 250, y = 200)

    select_button2 = tk.Button(window1, text = '选择图片', font = ('宋体', 12), width = 8, height = 1, command = print_image_selection)
    select_button2.place(x = 50, y = 200)

    transfer_botton = tk.Button(window1, text = '开始转换', font = ('宋体', 12), width = 8, height = 1, command = transfer)
    transfer_botton.place(x = 150, y = 200)

    window1.mainloop()

if __name__ == '__main__':
    main()