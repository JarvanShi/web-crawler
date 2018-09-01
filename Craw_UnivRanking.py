import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(uri):
    try:
        r = requests.get(uri ,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        return html
    except:
        return '产生异常'

def fillUnivList(html ,uList):
    soup = BeautifulSoup(html , 'html.parser')
    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            uList.append([tds[0].string , tds[1].string , tds[2].string , tds[3].string])
    return uList

def printUnivList(uList ,num):
    print('{0:<5}\t{1:{4}<8}\t{2:^8}\t{3:<5}'.format('排名','学校名称','省市','总分',chr(12288)))
    for i in range(num):
        u = uList[i]
        print('{0:<5}\t{1:{4}<8}\t{2:^8}\t{3:<5}'.format(u[0],u[1],u[2],u[3],chr(12288)))

def main():
    uri = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    uInfo = []
    num = 20
    html = getHTMLText(uri)
    fillUnivList(html , uInfo)
    printUnivList(uInfo ,num)

main()