import requests
from bs4 import BeautifulSoup  #bs4库的编码为utf-8

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers = kv)
        r.raise_for_status()  #连接成功继续执行，否则执行except
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

url = 'https://www.python123.io/ws/demo.html'
demo = getHTMLText(url)  # 标签树
soup_1 = BeautifulSoup(demo ,'html.parser')

# demo可以直接替换为一个html格式的数据
soup_2 = BeautifulSoup('<p>中国</p>','html.parser')

# BeautifulSoup类的基本元素
tag = soup_1.a  # 标签a
print(tag.name) # 标签名
print(tag.attrs)  # 标签属性
print(type(tag.attrs)) # 标签属性的类型（字典）
print(tag.string)  # 标签包含的字符串信息
print(tag.comments)  # 标签的注释信息 注释的格式<!--data-->
print(soup_1.prettify()) # 在每一个标签后添加换行符，调用print函数时，使结果显示更加友好

# 基于bs4库的HTML内容遍历方法
# 向上遍历
soup_1.title.parent # title的父节点
soup_1.title.parents  #title的所有先辈节点，迭代类型

# 处理节点为空的情形
for parent in soup_1.title.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# 向下遍历
print(soup_1.head.contents)  # 子节点的列表信息
soup_1.head.children # 子节点的迭代类型，可以用于循环遍历子节点
soup_1.head.descendants  #子孙节点的迭代类型，可以用于循环遍历子孙节点

# 平行遍历 （平行遍历发生于同一个父节点之下,且如果节点中有string类型，此类型会被识别为节点）
soup_1.a.next_sibling  # 下一个平行节点
soup_1.a.previous_sibling # 上一个平行节点
soup_1.a.next_siblings  # 迭代类型
soup_1.a.previous_siblings  # 迭代类型