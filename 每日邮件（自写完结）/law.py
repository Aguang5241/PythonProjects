import requests
import re
from bs4 import BeautifulSoup

def get_law(url, headers):
    html = requests.get(url, headers = headers).content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    views = []
    view_list = soup.find_all('h2', 'headline')
    for view in view_list:
        view_title = view.find('a').get_text()
        view_a = view.find('a')
        view_link = view_a['href']
        views.append([view_title, view_link])

    news = []
    new_list = soup.find_all('p', 'pis-title')
    for new in new_list:
        new_title = new.find('a').get_text()
        new_a = new.find('a')
        new_link = new_a['href']
        news.append([new_title, new_link])
    
    yield{
        'view': views,
        'new': news
    }
        

def main():
    url = 'http://conflictoflaws.net'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
    }
    
    law = get_law(url, headers)
    for _ in law:
        print(_)


if __name__ == '__main__':
    main()