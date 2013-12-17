# -*- coding: utf-8 -*-
'''

'''
from threading import Thread
import redis
class RedisThread(Thread):
    
        
    def testRelease(self):
        re = redis.Redis(connection_pool = pool)
        #connCount(re)
        print len(re.client_list())
        pool.release(re)
        
    def run(self):
        self.testRelease()
       
        #print "thread  thest..."
        
pool = redis.ConnectionPool(host="127.0.0.1", port=6579)
t = RedisThread()
t2 = RedisThread()
t3 = RedisThread()
t4 = RedisThread()

t.start()
t4.start()
t3.start()
t2.start()