import requests
import re

def getPage(uri):
    try:
        r = requests.get(uri, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

def parsePage(page, infoList):
    try:
        regex_p = re.compile(r'\"view_price"\:\"[\d\.]*\"')
        regex_t = re.compile(r'\"raw_title\"\:\".*?\"')
        Lst_p = regex_p.findall(page)
        Lst_t = regex_t.findall(page)
        for i in range(len(Lst_p)):
            price = eval(Lst_p[i].split(':')[1])
            title = eval(Lst_t[i].split(':')[1])
            infoList.append([price,title])
    except:
        return ''

def printPage(infoList):
    layout = '{:<4}\t{:<8}\t{:<16}\t'
    print(layout.format('序号','价格','商品名称'))
    count = 0
    for g in infoList:
        count += 1
        print(layout.format(count,g[0],g[1]))

def main():
    goods = '书包'
    start_uri = 'http://s.taobao.com/search?q=' + goods
    infoList = []
    depth = 3
    for i in range(depth):
        try:
            uri = start_uri + str(44*i)
            page = getPage(uri)
            parsePage(page, infoList)
        except:
            continue
    printPage(infoList)

main()