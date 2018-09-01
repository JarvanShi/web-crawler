import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(uri, encoding = 'utf-8'):
    try:
        r = requests.get(uri)
        r.raise_for_status()
        r.encoding = encoding
        return r.text
    except:
        return ''

def getStockList(stock_list_uri, stock_list, fpath):
    page = getHTMLText(stock_list_uri, 'GB2312')
    soup = BeautifulSoup(page, 'html.parser')
    a_parent = soup.find_all('div', attrs= {'class':'qox'})
    for a in a_parent.find_all('a'):
        try:
            href = a.attrs['href']
            regex =re.compile(r'[s][hz]\d{6}')
            stock_list.append(regex.findall(href)[0])
        except:
            continue
    with open(fpath, 'a', encoding='utf-8') as fun:
        fun.write(str(stock_list))
        fun.close()

def getStockInfo(stock_info_uri, stock_list, fpath):
    count = 0
    for stock in stock_list:
        uri = stock_info_uri + stock + '.html'
        page = getHTMLText(uri)
        try:
            if page == '':
                count += 1
                print('\r当前进度:{:.2f}%'.format(count*100/len(stock_list)),end='')
                continue
            stockInfo = {}
            soup = BeautifulSoup(page, 'html.parser')
            stock_info = soup.find('div', attrs= {'class':'stock-bets'})

            name = stock_info.find_all(attrs= {'class':'bets-name'})[0]
            stockInfo.update(name.text.split()[0])

            keyList = stock_info.find_all('dt')
            valList = stock_info.find_all('dd')
            for i in keyList:
                key = keyList[i].text
                val = valList[i].text
                stockInfo[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(stockInfo) + '\n')
                count += 1
                print('\r当前进度:{:.2f}%'.format(count*100/len(stock_list)),end='')
        except:
            count += 1
            print('\r当前进度:{:.2f}%'.format(count * 100 / len(stock_list)), end='')
            continue

def main():
    stock_list_uri = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_uri = 'https://gupiao.baidu.com/stock/'
    stock_list_fpath = 'E:/stockList.txt'
    stock_info_fpath = 'E:/stockInfo.txt'
    sList = []
    getStockList(stock_list_uri, sList, stock_list_fpath)
    getStockInfo(stock_info_uri, sList, stock_info_fpath)
main()