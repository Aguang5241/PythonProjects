import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import urllib.request

def main():
    window = tk.Tk()
    window.geometry('300x150')
    window.title('下载小喵喵')
    l1 = tk.Label(window, text = '请填写图片尺寸', font = ('宋体', 16))
    l1.pack()
    l2 = tk.Label(window, text = '宽', font = ('宋体', 16))
    l2.place(x = 0, y = 40)
    l3 = tk.Label(window, text = '高', font = ('宋体', 16))
    l3.place(x = 0, y = 70)

    e1 = tk.Entry(width = 35)
    e1.place(x = 30, y = 40)
    e2 = tk.Entry(width = 35)
    e2.place(x = 30, y = 70)

    def ok_button():
        width = int(e1.get())
        height = int(e2.get())
        path = tk.filedialog.askdirectory()
        url = 'http://placekitten.com/%s/%s' % (width, height)
        req = urllib.request.urlopen(url)
        req.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400')]
        img = req.read()
        with open(r"%s/cat_%dx%d.jpg" % (path, width, height), 'wb') as f:
            f.write(img)
        tk.messagebox.showinfo(title='', message='下载完成')


    def cancel_button():
        window.quit()

    b1 = tk.Button(window, text = 'OK', font = ('Arail', 14), width = 6, command = ok_button)
    b1.place(x = 50, y = 100)
    b2 = tk.Button(window, text = 'Cancel', font = ('Arail', 14), width = 6, command = cancel_button)
    b2.place(x = 160, y = 100)

    window.mainloop()

if __name__ == '__main__':
    main()