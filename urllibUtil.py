#coding:gbk
'''
urllib util ץȡ��ҳ��Ϣ
'''

import urllib

'''
�÷���ֻҪ����ץȡ��ҳ�����ݣ�������������Ϣ
urlopen()�������صĶ��� ӵ�еķ�����
close()
read(),readline(), readlines()
'''
def getContent(url):
    webPage = urllib.urlopen(url)
    content = webPage.readlines()
    webPage.close()
    return content

'''
������Ϣ������ͼƬ
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