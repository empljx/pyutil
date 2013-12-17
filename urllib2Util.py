# -*- coding: gbk -*-
'''

'''

import urllib2
import urllib
url = "http://127.0.0.1:5000/"
#url = "http://www.google.com"
'''
urlopen() �������ص�response����:
1. read()    ����ֵ��str
2. readline() ����ֵ��str
3. readlines() ����ֵ�Ǹ�list
4. close()
5. headers
6. geturl() ��ʵ��url, ��ת���url
7. info() == headers ͷ����Ϣ
'''

def one():
    res = urllib2.urlopen(url)
    print res.geturl()
    print "info"
    print res.info()
    print "headers"
    print res.headers
    html = res.read()
    res.close()
    print html

def two():
    request = urllib2.Request(url)
    res = urllib2.urlopen(request)
    print res.__doc__
    print res.__dict__
    print "fp:"
    print res.fp
    print "fileno"
    print res.fileno()
    print res.headers
    html = res.readlines()
    for h in html:
        print h

'''
urllib.urlencode ���б���, ��data:��post�����;������get����
'''
def urlParamPost():
    query = {"name":"dd"}
    data = urllib.urlencode(query)
    print data
    request = urllib2.Request(url, data)
    res = urllib2.urlopen(request)
    print res.read()
    print res.url
    res.close()

'''
urllib.urlencode ���б���, ���ַ�ʽ��post�����
'''
def urlParamGet():
    url33 = url + "?" + "name=dd"
    print url33
    request = urllib2.Request(url33)
    res = urllib2.urlopen(request)
    if res.code == "200":
        print res.read()
        print res.url
    elif res.code == "404":
        print "wrong..........."
        
    res.close()   

'''
urllib2.URLError �쳣
e.reason �����ԭ��
e.code
'''    
def urlError():
    try:
        urlParamGet()
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
    except urllib2.HTTPError, e:
        print e
        print "http code:", e.code
        print e.reason
    except urllib2.URLError, e:
        print e
        print e.reason
        print e.code

'''
����Щ header Ҫ�ر����⣬�������������Щ header �����
User-Agent : ��Щ�������� Proxy ��ͨ����ֵ���ж��Ƿ������������������
Content-Type : ��ʹ�� REST �ӿ�ʱ�������������ֵ������ȷ�� HTTP Body �е����ݸ�����������������ȡֵ�У�
application/xml �� �� XML RPC���� RESTful/SOAP ����ʱʹ��
application/json �� �� JSON RPC ����ʱʹ��
application/x-www-form-urlencoded �� ������ύ Web ��ʱʹ��
��ʹ�÷������ṩ�� RESTful �� SOAP ����ʱ�� Content-Type ���ô���ᵼ�·������ܾ�����

ĳЩվ������ν�ķ��������ã���ʵ˵���˺ܼ򵥣�
���Ǽ���㷢�������header���棬refererվ���ǲ������Լ���
��������ֻ��Ҫ���headers��referer�ĳɸ���վ���ɣ���cnbetaΪ����

headers��һ��dict���ݽṹ������Է����κ���Ҫ��header������һЩαװ��
���磬��Щ��վϲ����ȡheader�е�X-Forwarded-For�������˼ҵ���ʵIP������ֱ�Ӱ�X-Forwarde-For���ˡ�
'''
def requestUrl():
    #url = "http://10.16.0.238:8081/lottery/admin/getIp.action"
    url = "http://127.0.0.1:8080/admin/getIp.action"
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
               , "Referer": "http://www.baidu.com", "X-Forwarded-For":"1s2.45.51.235"}
    query = {"name":"fds"}
    data = urllib.urlencode(query)
    req = urllib2.Request(url=url, data = data, headers = headers)
    
    res = urllib2.urlopen(req)
    print res.read()
    
requestUrl()