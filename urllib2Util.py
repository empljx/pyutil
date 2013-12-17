# -*- coding: gbk -*-
'''

'''

import urllib2
import urllib
url = "http://127.0.0.1:5000/"
#url = "http://www.google.com"
'''
urlopen() 函数返回的response对象:
1. read()    返回值是str
2. readline() 返回值是str
3. readlines() 返回值是个list
4. close()
5. headers
6. geturl() 真实的url, 跳转后的url
7. info() == headers 头部信息
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
urllib.urlencode 进行编码, 加data:是post请求的;不加是get请求
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
urllib.urlencode 进行编码, 这种方式是post请求的
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
urllib2.URLError 异常
e.reason 具体的原因
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
对有些 header 要特别留意，服务器会针对这些 header 做检查
User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。常见的取值有：
application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
application/json ： 在 JSON RPC 调用时使用
application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务

某些站点有所谓的反盗链设置，其实说穿了很简单，
就是检查你发送请求的header里面，referer站点是不是他自己，
所以我们只需要像把headers的referer改成该网站即可，以cnbeta为例：

headers是一个dict数据结构，你可以放入任何想要的header，来做一些伪装。
例如，有些网站喜欢读取header中的X-Forwarded-For来看看人家的真实IP，可以直接把X-Forwarde-For改了。
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