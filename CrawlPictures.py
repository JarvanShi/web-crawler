import requests
import os

def getJpg(uri):
    try:
        r = requests.get(uri)
        r.raise_for_status()
        return r.content
    except:
        return '产生异常'

def downPicture(jpg ,path):
    try:
        if not os._exists(path):
            with open(path,'wb') as f:
                f.write(jpg)
                f.close()
                print('保存成功')
        else:
            return '文件已存在'
    except:
        return '下载失败'

def main():
    uri = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1528811162678&di=debe1c668454c83eb4deadc3d90ddf43&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F0381de85949053ca8012193a3339cc5.jpg'
    root = 'D:\\'
    path = root + 'temp.jpg'
    jpg = getJpg(uri)
    downPicture(jpg ,path)

main()