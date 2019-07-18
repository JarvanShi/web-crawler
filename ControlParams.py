import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(uri):
    try:
        # 修改头部信息
        # kv = {'user-agent': 'Mozilla/5.0'}
        # r = requests.get(uri, headers = kv)

        # 添加url参数
        # uri = 'http://www.baidu.com'
        # kv = {'wd':'python'}
        # r = requests.get(uri, params = kv)

        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return '产生异常'

def printHTML(html):
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify())

def main():
    # uri = 'https://item.jd.com/6946629.html'
    uri = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
    html = getHTMLText(uri)
    printHTML(html)

main()