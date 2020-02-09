'''
被反爬压制
'''

import requests
import re
import os
import time

def get_folder_url_and_name(url, headers):
    html = requests.get(url, headers = headers)
    html = html.text
    url_and_name = re.findall(r'<span>.*?<a href="(.*?)".*?target=.*?>(.*?)</a>.*?</span>', html, re.S)
    for url_name in url_and_name:
        yield{
            'folder_url' : url_name[0],
            'folder_name': url_name[1].strip()
        }

def get_img_url_page(url, headers):
    html = requests.get(url, headers = headers)
    html = html.text
    page = re.findall(r'<a href=.*?>.*?<span>(\d{2})</span>.*?</a>', html, re.S)
    url = re.findall(r'<a href=.*?>.*?<img src="(.*?)".*?</a>', html, re.S)
    yield {
        'url' : url[0],
        'page': int(page[0])
    }


def download(url, headers, folder_name): 
    pages   = url.get('page')
    img_url = url.get('url')[:-6] # https://i.meizitu.net/2019/06/26c
    os.chdir(folder_name)
    
    for page in range(pages):
        image_url = img_url + '%02d.jpg' % (page + 1) # https://i.meizitu.net/2019/06/26c23.jpg
        image = requests.get(image_url, headers = headers)
        image = image.text
        with open(image_url[-6:], 'a') as f:
            f.write(image)
            time.sleep(1)
        
def main():
    os.mkdir('mm_img')
    os.chdir('mm_img')

    url = 'https://www.mzitu.com/xinggan'
    global headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
    }
    folder_url_and_name = list(get_folder_url_and_name(url, headers))
    # [{'folder_url': 'https://www.mzitu.com/199385', 'folder_name': 'xxx'}, {}, {}]
    for folder in folder_url_and_name:
        folder_url  = folder.get('folder_url')
        folder_name = folder.get('folder_name')
        os.mkdir(folder_name)

        img_url_page = get_img_url_page(folder_url, headers)
        for url_page in img_url_page:
            # {'url': 'https://i.meizitu.net/2019/08/14a01.jpg', 'page': 60}
            download(url_page, headers, folder_name)

        
if __name__ == main():
    main()