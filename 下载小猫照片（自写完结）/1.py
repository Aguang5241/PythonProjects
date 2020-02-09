import requests


image_url1 = 'https://img.ivsky.com/img/bizhi/pre/201907/06/yuzhou_xingqiu.jpg'
image_url2 = 'https://i.meizitu.net/2019/08/17b01.jpg'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
}

image = requests.get(image_url2, headers = headers)

image = image.content
print('>>>', image, type(image), len(image))
with open('123.jpg', 'wb') as f:
    f.write(image)

