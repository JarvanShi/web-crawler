import requests
import time

# 爬虫代码框架
def getHTMLText(url):
    try:
        u_agent= {'user-agent':'Mozilla/5.0'}
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print('产生异常')

url = 'http://www.baidu.com'
num = int(input('输入爬取次数'))

# 统计爬虫时间
tempTime = []
for i in range(1,num + 1):
    startTime = time.perf_counter()
    getHTMLText(url)
    tempTime.append(time.perf_counter() - startTime)
    print('第%d次爬取时间：%.3f' %(i,tempTime[i - 1]))
    # print('第{}次爬取时间：{:.3f}'.format(i,tempTime[i - 1]))

print('总花费时间：%.3f' %sum(tempTime))