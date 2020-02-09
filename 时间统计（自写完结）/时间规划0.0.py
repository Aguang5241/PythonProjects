'''
读取CSV格式，分类并计算
类别有两类：日期+项目
计算指定多个时间下指定用时总共用时
'''

import csv

def main():
    go_on = True
    while go_on:
        file = input('输入文档：')
        filename = '%s.csv' % file
        # 先筛选项目
        items = ['学习', '工作', '睡眠', '娱乐其他'] 
        # 将筛选后的所有数据分给下面四个列表
        # 以下数据均为[[]]形式
        study_dates = []  
        work_dates = []
        sleep_dates = []
        other_dates = [] 
        # 在各个列表中筛选用户输入的日期，分给下面的列表
        # 此列表含有指定日期的所有信息
        dates_data = []
        # 先求交集，后加和
        item_dates_list = []
        total = 0.0

        def combine(list1, list2):
            list3 = []
            for i in list1:
                for j in list2:
                    if i == j:
                        list3.append(i)
            return list3
        
        # 项目类别输入   
        index = 0
        while True:
            try:
                index = int(input('输入项目编号【1.学习；2.工作；3.睡眠；4.娱乐其他】：'))
            except ValueError:
                pass
            finally:
                if 0 < index < 5:
                    break
                else:
                    print('输入有误，请重新', end = '')
        # 查询日期集合
        dates = []
        # 处理用户日期输入——月
        m = 0
        while True:
            try:
                m = int(input('输入要查询的月份（1-12）：'))
            except ValueError:
                pass
            finally:
                if 0 < m < 10:
                    m = '0' + str(m)
                    break
                elif 10 <= m <= 12:
                    m = str(m)
                    break
                else:
                    print('错误，请重新', end = '')
        # 处理用户日期输入——日
        d = 0   
        while True:
            try:
                d = int(input('输入要查询的日期（1-31）【输入886结束】：'))
            except ValueError:
                pass
            finally:
                if 0 < d < 10:
                    d = '0' + str(d)
                    date_input = '%s-%s' % (m, d)       
                    dates.append(date_input)
                elif 10 <= d <= 31:
                    d = str(d)
                    date_input = '%s-%s' % (m, d)       
                    dates.append(date_input)
                elif d == 886:
                    break
                else:
                    print('输入有误，请重新', end = '')


        try:
            with open(filename,encoding = 'utf-8') as f:
                reader = csv.reader(f)
                data = list(reader)

        except FileNotFoundError:
            print('|--------------------------------------------------|')
            print('|--------------------找不到文件--------------------|', filename)
            print('|--------------------------------------------------|')
        else:
            for item in data:
                if item[0] == items[0]:
                    study_dates.append(item)
                if item[0] == items[1]:
                    work_dates.append(item)
                if item[0] == items[2]:
                    sleep_dates.append(item)
                if item[0] == items[3]:
                    other_dates.append(item)
                
                for date in dates:
                    if date in item[2]:
                        dates_data.append(item)
                    
            if index == 1:
                item_str = '学习'
                item_dates_list = combine(dates_data, study_dates)
            elif index == 2:
                item_str = '工作'
                item_dates_list = combine(dates_data, work_dates)
            elif index == 3:
                item_str = '睡眠'
                item_dates_list = combine(dates_data, sleep_dates)
            else:
                item_str = '娱乐其他'
                item_dates_list = combine(dates_data, other_dates)

            # len(item_dates_list[0][1])) == 5 ; type(item_dates_list[0][1])) == str
            for row in item_dates_list:
                str0 = row[1]
                hour = str0[0:2]
                minute = str0[3:5]
                h = int(hour)
                m = int(minute)
                # 数据转换：时间转浮点
                num = float('%.2f' % (h + m / 60))
                # 进行计算时间
                total += num
            hours = int(total)
            minutes = int((total - hours) * 60 + 0.5)
            if total == 0.0:
                print('|--------------------------------------------------|')
                print('|------------------未找到匹配信息------------------|')
                print('|--------------------------------------------------|')
            else:
                print('|--------------------------------------------------|')
                print('| 你所查询的日期中 “%s” 共用了 %d 小时 %d 分钟 |' % (item_str, hours, minutes))
                print('|--------------------------------------------------|')
        
        keep_check = input('输入y继续>>> ')
        if keep_check == 'y' or 'Y':
            pass
        else:
            go_on = False
 
if __name__ == '__main__':
    main()