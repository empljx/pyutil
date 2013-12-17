# -*- coding: utf-8 -*-

import socket
from time import ctime

def hostInfo():
    hostName = socket.gethostname()
    print hostName
    print socket.gethostbyname(hostName)
    print socket.gethostbyname_ex(hostName)
    print socket.getfqdn(hostName)
    print socket.getaddrinfo("www.baidu.com", 80)

def getIp(host):
    # host 可以是网址
    socket.gethostbyname(host)
    

def tcpServerSender():
    serSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("127.0.0.1", 12345)
    serSock.bind(addr)
    serSock.listen(11)
    
    while True:
        print "waiting for clients coming...."
        
        conn, addrHost = serSock.accept()
        print "...connection from :", addrHost
        
        while True:
            data = conn.recv(1024)
            print "receive data:", data
            
            if not data:
                break
            conn.send("%s, %s" % (ctime(), data))
            print conn.getpeername()
            print conn.getsockname()
            
        conn.close()
        print "connection closed..."
    serSock.close()

def udpServerSender():
    serSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ("127.0.0.1", 12345)
    serSock.bind(addr)
    
    while True:
        print "waiting for clients coming...."
        data, hostAddr = serSock.recvfrom(1024)
        print "receive data:", data, hostAddr
        
        serSock.sendto("%s, %s" % (ctime(), data), hostAddr)
            
    serSock.close()
                   
hostInfo()
                