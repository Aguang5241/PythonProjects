import requests
import re

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
}


url = 'https://s.weibo.com/top/summary?cate=realtimehot'
weibo_text = []
html = requests.get(url, headers = headers).content.decode('utf-8')
# print(html)
titles_links = re.findall(r'<td class=.*?>.*?<a href="(.*?)" target=.*?>(.*?)</a>.*?</td>', html, re.S)
for title_link in titles_links:
    weibo_text.append({
    'title': title_link[1],
    'link' : 'https://s.weibo.com' + title_link[0]
    })
print(weibo_text)
