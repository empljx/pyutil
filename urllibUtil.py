#coding:gbk
'''
urllib util 抓取网页信息
'''

import urllib

'''
该方法只要勇于抓取网页的数据，不进行下载信息
urlopen()方法返回的对象 拥有的方法：
close()
read(),readline(), readlines()
'''
def getContent(url):
    webPage = urllib.urlopen(url)
    content = webPage.readlines()
    webPage.close()
    return content

'''
下载信息，不如图片
'''
def downloadInfo(url, filename):
    urllib.urlretrieve(url, filename)
    
if __name__ == "__main__":
    url = ""
    content = getContent(url)
    print content
    
    img = ""
    filename = ""
    downloadInfo(img, filename)