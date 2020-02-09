import tkinter as tk
from PIL import Image
# filedialog是tkinter模块下的一个子模块，并不是他的函数和性质
# 不能直接去调用filedialog模块下的函数,需要引入子模块filedialog，再去使用它的函数。
from tkinter import filedialog




def main():
    window = tk.Tk()
    window.title('图片格式转换精灵（v1.1）')
    window.geometry('400x300')

    # 设置提示标签  
    l1 = tk.Label(window, bg = 'green', font = ('宋体', 18), width = 50, text = '请选择转换格式')
    l1.pack()
    l2 = tk.Label(window, bg = 'red', font = ('宋体', 16), width = 50, text = 'None')
    l2.pack()

    # 设置路径标签
    l3 = tk.Label(window, bg = 'blue', font = ('Arial', 12), width = 34, text = '')
    l3.place(x = 0, y = 150)
    l4 = tk.Label(window, bg = 'blue', font = ('Arial', 12), width = 34, text = '')
    l4.place(x = 0, y = 200)


    # 打开文件 + 格式转换 + 保存文件
    image_type = ['.jpg', '.png', '.tif', '.gif']
    global index, path_old, path_new
    index = 0
    path_old = ''
    path_new = ''
        
    class Button_hit():
        def b1_selected():
            l2.config(text = '已选择JEPG')
            index = 0
 
        def b2_selected():
            l2.config(text = '已选择PNG')
            index = 1


        def b3_selected():
            l2.config(text = '已选择TIF')
            index = 2

        def b4_selected():
            l2.config(text = '已选择GIF')
            index = 3

        def get_path_old():
            path_old = tk.filedialog.askopenfilename(title = u'选择图片')
            l3.config(text = path_old)         
        def get_path_new(): 
            path_new = tk.filedialog.asksaveasfilename(title = u'另存为')
            l4.config(text = path_new)

    def transfer():
        img = Image.open(path_old)
        img.save('%s%s' % (path_new, image_type[index]))

    b1 = tk.Button(window, text = 'JEPG', font = ('Times New Roman', 12), width = 5, height = 1, command = Button_hit.b1_selected)
    b1.place(x = 50, y = 70)

    b2 = tk.Button(window, text = 'PNG', font = ('Times New Roman', 12), width = 5, height = 1, command = Button_hit.b2_selected)
    b2.place(x = 130, y = 70)

    b3 = tk.Button(window, text = 'TIF', font = ('Times New Roman', 12), width = 5, height = 1,command = Button_hit.b3_selected)
    b3.place(x = 210, y = 70)

    b4 = tk.Button(window, text = 'GIF', font = ('Times New Roman', 12), width = 5, height = 1, command = Button_hit.b4_selected)
    b4.place(x = 290, y = 70)

    b5 = tk.Button(window, text = '选择图片', font = ('宋体', 12), width = 8, height = 1, command = Button_hit.get_path_old)
    b5.place(x = 320, y = 150)

    b6 = tk.Button(window, text = '另存为', font = ('宋体', 12), width = 8, height = 1, command = Button_hit.get_path_new)
    b6.place(x = 320, y = 200)

    b7 = tk.Button(window, text = '开始转换', font = ('宋体', 12), width = 8, height = 1, command = transfer)
    b7.place(x = 170, y = 250)

    window.mainloop()

if __name__ == '__main__':
    main()