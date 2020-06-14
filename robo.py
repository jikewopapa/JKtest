from urllib.parse import  urljoin
import requests







class Robots:
    def __init__(self,url,Agent):
        self.Baseurl=url
        self.url=url
        self.heads={
    'User-agent':Agent,
}
        self.ends = 'robots.txt'
        self.dourl()
        self.GetRobots

    def dourl(self):
        url=self.url.split('/')
        url='/'.join(url[:3])
        url = urljoin(url, self.ends)
        self.url=url


    def GetRobots(self):
        html = requests.get(url=self.url)

        with open('robots.txt', 'w', encoding='utf8') as f:
            f.write(html.text)

        with open('robots.txt', 'r', encoding='utf8') as f:
            lines = f.readlines()
            flag = False
            domain = []
            for line in lines:

                line = line.strip().replace('\n', '')
                if self.heads['User-agent'] in line:
                    flag = True
                    continue
                elif line.startswith('Disallow'):
                    if flag:
                        domain.append(line.replace('Disallow: ',''))
                elif line is None or line == '':
                    if flag:
                        break


        for d in domain:
            if d in self.Baseurl:
                print(d)

                return False

        print("网站允许爬")
        return True

if __name__ == '__main__':
    url='https://www.baidu.com/s?wd=she&ie=UTF-8'

    r=Robots(url,'Baiduspider-image')
    t=r.GetRobots()
    if t:
        print("网站允许爬")
    else:

        print("网站禁止爬")