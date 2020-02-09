from bs4 import BeautifulSoup
from matplotlib import pyplot
import datetime

def data(item):
    def cal(i):
        hour = int(i[:2])
        minute = int(i[3:])
        time = hour + minute/60
        return time
    
    def span(start, end):
        d1 = datetime.datetime.strptime(start, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(end, '%Y-%m-%d')
        date_span = d1 - d2
        return date_span.days

    def span_list(start, end, time_span):
        datestart = datetime.datetime.strptime(end, '%Y-%m-%d')
        dateend=datetime.datetime.strptime(start,'%Y-%m-%d')
        time_span_list = []
        time_span_list.append([datestart.strftime('%Y-%m-%d')])
        while datestart<dateend:
            datestart+=datetime.timedelta(days=+1)
            time_span_list.append([datestart.strftime('%Y-%m-%d')])
        return list(reversed(time_span_list))

    # 处理第二项内容    
    item.pop()
    for each in item:
        each[1] = each[1][:10]
    
    # 按时间重新分组
    date_time = [[[item[0][1],item[0][3]]]]
    while True:
        if len(item)>1:
            target = [item[1][1],item[1][3]]
            if item[0][1] in item[1]:
                date_time[len(date_time)-1].append(target)
                item.pop(0)
            else:
                date_time.append([target])
                item.pop(0)
        else:
            date_time[len(date_time)-1].append(target)
            break

    # 重整
    time_date = []
    for each in date_time:
        time_total = 0.0
        time_total_list = [each[0][0]]
        for i in each:
            time_str = i[1]
            time = cal(time_str)
            time_total += time
        time_total_list.append('%.2f' % time_total)
        time_date.append(time_total_list)
    
    # 继续重整，补充未记录日期数据
    start = time_date[0][0]
    end = time_date[-1][0]
    time_span = span(start, end)
  
    # 生成一个完整的日期跨度列表[[xxxx-xx-xx],[],...,[]]
    time_span_list = span_list(start, end, time_span)

    # 补充数据
    for td in time_date:
        date_td, time_td = td[0], td[1]
        for tsl in time_span_list:
            if tsl[0] == date_td:
                tsl.append(time_td)
    
    # 简化日期格式
    for each in time_span_list:
        each[0] = each[0][-5:]
    
    return time_span_list

    # 算法慢的感人！！！！
    # for i in range(length_item):
    #     length_data = len(item_data)
    #     for j in range(length_data):
    #         if item[i][1] == item[i+1][1]:
    #             item_data[j] += cal(i+1)
    #         else:
    #             item_data.append(cal(i+1))

def draw(item):
    date_list = []
    time_list = []
    for each in item:
        if len(each) == 2:
            time_list.append(float(each[1]))
        if len(each) ==1:
            time_list.append(0)
        date_list.append(each[0])
    date_list.reverse()
    time_list.reverse()
    pyplot.bar(date_list, time_list, align='center', color='g')
    pyplot.title('Time Analyse')
    pyplot.ylabel('Time Spend(h)')
    pyplot.xlabel('Date')
    pyplot.xticks(date_list, rotation=60)
    pyplot.show()    

def main():
    list_items = []
    study, work, sleep, other = [], [], [], [] 
    with open('report.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    for td in soup.select('td'):
        if td.get_text() != '':
            list_items.append(td.get_text())
    list_item = [list_items[i:i+4] for i in range(0, len(list_items), 4)]
    
    for each in list_item:
        if '学习' in each:
            study.append(each)
        if '工作' in each:
            work.append(each)
        if '睡眠' in each:
            sleep.append(each)
        if '娱乐其他' in each:
            other.append(each)

    while True:
        command_id = input('输入查询类别序号【1.学习】【2.工作】【3.睡眠】【4.其他】')
        if command_id == '1':
            command = study
        if command_id == '2':
            command = work
        if command_id == '3':
            command = sleep
        if command_id == '4':
            command = other

        draw(data(command))

if __name__ == '__main__':
    main()
