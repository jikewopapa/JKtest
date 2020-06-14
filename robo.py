from urllib.parse import  urljoin


url='https://www.baidu.com/s?wd=she&ie=UTF-8'
ends='robots.txt'

url=url.split('/')
url='//'.join(url[:3])
print(url)