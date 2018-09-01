import requests  # requests库的主要方法：request get head post put patch delete

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

uri = 'http://www.python123.io/ws/demo.html'
demo = getHTMLText(uri)