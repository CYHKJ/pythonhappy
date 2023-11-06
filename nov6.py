# 암호 처리

""" import getpass

pw = input("pass :")

#pw = getpass.getpass("Pass :")

print(pw)
 """


# 해시 함수 

""" import hashlib

hl = hashlib.sha256()
target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "media program"
#target = "123456789"
#target = "to be or not to be, That is a question"

hl.update(target.encode("utf-8"))

print(hl.hexdigest())
#print(hl.digest()) """


# keccak256

""" import Crypto.Hash.keccak as kek
target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "media program"
#target = "123456789"
#target = "to be or not to be, That is a question"
kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest())
print(kksh.digest()) """


# 활용

""" import getpass
import hashlib

pw = getpass.getpass("Pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest()) """


# 암호 파일 저장

""" import os
import hashlib

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input(' insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True
    
    
if pwInsert():
        pw = input('new pass :')
        with open('pw.txt', 'w') as fp:
            hs = hashlib.sha256()     
            hs.update(pw.encode("utf-8"))
            fp.write(hs.hexdigest())
else:
    print("not allow password") """


# 시스템 정보 확인 

""" import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps) """


# 웹페이지 읽기 

""" import urllib.request as ur

url = 'https://www.google.com'
#url = "http://www.daum.net"
#url = "http://xkcd.com/"

res = ur.urlopen(url)
web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)

print(web) """


""" import http.client as hc

url = "www.google.com"
#url = 'https://www.google.com'
#url = "http://www.daum.net"
#url = "http://xkcd.com/"

conn = hc.HTTPSConnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulcl.html", "wb") as fp:
    fp.write(r.read())

conn.close()

print(r) """


""" import requests 

url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web)
    
print(web) """


# 싱글스레드

""" import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
for i in range(3) :
    counter(f"num{i}")
    
end = time.time()    

print("single end", end - start)  """


# 멀티 스레드 

""" import threading
import time


def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

thread1 = threading.Thread(target=counter, args=("1num",))
thread2 = threading.Thread(target=counter, args=("2num", ))
thread3 = threading.Thread(target=counter, args=("3num", ))

start = time.time()
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time() 

print("multi end", end - start)
 """


# 멀티 프로세싱

""" import multiprocessing
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
 
process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))


start = time.time()
process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time() 

print("processing end", end - start) """


# main 실행 

def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    run()








