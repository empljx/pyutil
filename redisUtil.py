# -*- coding: utf-8 -*-
'''
three ways:
pip install redis
easy_install redis
python setup.py install
'''

'''
redis链接方法有些redis的命令实现不一样。
比如del -> delete()
https://pypi.python.org/pypi/redis/2.8.0
'''
import redis

def connPool():
    pool = redis.ConnectionPool(host="127.0.0.1", port=6579)
    return pool

'''
Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。
'''
def one():
    re = redis.Redis(host="127.0.0.1", port=6579)
    keyList = re.keys("*")
    for key in keyList:
        print key

def oneWithPool():
    pool = connPool()
    #pool = redis.ConnectionPool(host="127.0.0.1", port=6579)
    re = redis.Redis(connection_pool = pool)
    connCount(re)
    print re.llen("count")
    pool.release(re)
    connCount(re)

def two():
    re = redis.StrictRedis(host="127.0.0.1", port=6579)
    keyList = re.keys("*")
    for key in keyList:
        print key

def connCount(re):
    for r in re.client_list():
        print r

def testRelease(pool):
    re = redis.Redis(connection_pool = pool)
    #connCount(re)
    print len(re.client_list())


