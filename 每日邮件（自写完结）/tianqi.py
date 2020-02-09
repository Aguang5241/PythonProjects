import requests
import re
from bs4 import BeautifulSoup

def get_tianqi(url, headers):
    lanzhou_url = url + 'weather/101160101.shtml'
    changsha_url = url + 'weather/101250101.shtml'
    nanjing_url = url + 'weather/101190101.shtml'
    hainan_url = url + 'weather/101310101.shtml'
    url_pool = [lanzhou_url, changsha_url, nanjing_url, hainan_url]
    weathers = []
    for item in url_pool:
        weather = []
        html = requests.get(item, headers).content.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        day_list = soup.find('ul', 't clearfix').find_all('li')
        for day in day_list:
            date = day.find('h1').get_text()
            wea = day.find('p',  'wea').get_text()
            if day.find('p', 'tem').find('span'):
                    hightem = day.find('p', 'tem').find('span').get_text()
            else:
                    hightem = ''
            lowtem = day.find('p', 'tem').find('i').get_text()
            weather.append([date, wea, hightem, lowtem])
        weathers.append(weather)
    return weathers
    #[[[]*7]*4]

def main():
    url = 'http://www.weather.com.cn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
    }
    tianqi = get_tianqi(url, headers)
    print(tianqi)
    

if __name__ == '__main__':
    main()