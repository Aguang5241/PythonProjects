import time
import tkinter as tk
from tkinter import messagebox

def main():
    window1 = tk.Tk()
    window1.title('计时器【v0.0】')
    window1.geometry('300x200')

    l1 = tk.Label(window1, text = '当前时间：', font = ('宋体', 15))
    l1.place(x = 5, y = 10)
   
    def time_now():
        global seconds_now
        seconds_now = time.time()
        lt = time.localtime(seconds_now)
        time1 = []
        time2 = '%04d年%02d月%02d日    \n    %02d时%02d分%02d秒' % (lt[0], lt[1], lt[2], lt[3], lt[4], lt[5])

        if time2 != time1:
            time1 = time2
            l1_2 = tk.Label(window1, text = time1, font = ('宋体', 20))
            l1_2.configure(text = time2)
            l1_2.place(x = 30, y = 50)
            l1_2.after(200, time_now)
            
    time_now()
    
    def input_time():
        window2 = tk.Tk()
        window2.title('计时器【v0.0】')
        window2.geometry('300x120')

        l2_1 = tk.Label(window2, text = '年', font = ('宋体', 15))
        l2_1.place(x = 90, y = 20)
        l2_2 = tk.Label(window2, text = '月', font = ('宋体', 15))
        l2_2.place(x = 170, y = 20)
        l2_3 = tk.Label(window2, text = '日', font = ('宋体', 15))
        l2_3.place(x = 250, y = 20)
        l2_4 = tk.Label(window2, text = '有效日期【1970/1/2-3001/1/1】', font = ('宋体', 10))
        l2_4.place(x = 50, y = 50)

        year = tk.Entry(window2, text = None, font = ('宋体', 15), width = 5)
        month = tk.Entry(window2, text = None, font = ('宋体', 15), width = 5)
        day = tk.Entry(window2, text = None, font = ('宋体', 15), width = 5)
        year.place(x = 40, y = 20)
        month.place(x = 120, y = 20)
        day.place(x = 200, y = 20)

        def get_time():
            try:
                y = int(year.get())
                m = int(month.get())
                d = int(day.get())
                lt_ = time.strptime(f'{y} {m} {d}', '%Y %m %d')
                seconds_get = time.mktime(lt_)
            except BaseException:
                tk.messagebox.showerror(message='输入有误！')
            else:
                window2.withdraw()    
            
            string1 = '查询日期距离现在还有：'
            string2 = '查询日期距离现在已过去：'

            seconds_lasting = seconds_get - seconds_now
            
            day_lasting = abs(seconds_lasting) // 86400
            month_lasting = 0
            year_lasting = 0
            days = day_lasting
           
            if day_lasting > 356:
                year_lasting = day_lasting // 365
                day_lasting -= year_lasting * 365
                if day_lasting > 30:
                    month_lasting = day_lasting // 30
                    day_lasting -= month_lasting * 30
            elif day_lasting > 30:
                year_lasting = 0
                month_lasting = day_lasting // 30
                day_lasting -= month_lasting * 30 
            else:
                year_lasting, month_lasting = 0, 0
            
            if seconds_lasting > 0:
                prompt = string1
                days += 1
                day_lasting += 1
            else: 
                prompt = string2  
                  
            tk.messagebox.showinfo(message='%s%d天\n大概为%d年%d月%d天' % (prompt, days, year_lasting, month_lasting, day_lasting))   
                
        button2 = tk.Button(window2, text = '开始查询', font = ('宋体', 15), command = get_time)
        button2.place(x = 110, y = 75)
       
        window2.mainloop()

    button1 = tk.Button(window1, text = '输入查询日期', font = ('宋体', 15), command = input_time)
    button1.place(x = 85, y = 125)

    window1.mainloop()

if __name__ == '__main__':
    main()