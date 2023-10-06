#callback함수
""" def prt_func() :
    print("hello")

def callfunc(fx) :
		fx()

callfunc(prt_func) """

# 0 ~ 5 까지 숫자 나오게 하기
""" def prt_func(n):
    print("hello", n)
    
def callfunc(fx):
    for i in range(6):
        fx(i)
callfunc(prt_func) """

#Type Hint

""" def update_msg(name: str) -> list:
    msg = []
    msg.append("hello," + name)
    msg.append("bye," + name)
    return msg
    
def greeting(in_name: str) -> list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg

res = greeting("python")

for message in res:
    print(message) """

#재귀함수 

""" def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    
fun(1) """

#Factorial

""" def ploop(n):
    if n ==0:
        print("end")
        return 1
    else:
        print(n, n-1, "=", n + n-1)
        return n * ploop(n-1)
     
print(ploop(3)) """

#피보나치 수열

""" def fibonacci(n):
    if n ==0:
        return 0 
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    
res = fibonacci(4)
print("res =", res) """


#모듈

#사용 가능 메소드

""" import calc

print(dir(calc)) """

#calc 모듈 호출

""" import calc

#res = calc.add(8, 4)
#print(res)
print(calc.add(8, 4))
print(calc.sub(8, 4))
print(calc.mul(8, 4))
print(calc.div(8, 4)) """

#alias 사용
""" import calc as cl

#res = calc.add(8, 4)
#print(res)
print(cl.add(8, 4))
print(cl.sub(8, 4))
print(cl.mul(8, 4))
print(cl.div(8, 4)) """

# circle mod

""" import mod.circle_mod as cm
print(cm.pi)

print(cm.cc_area(4))
print(cm.cc_len(5)) """

# 문자열 자르기

""" def cutstr(st, wd, idx):
    tmp = st.split(wd)
    res = tmp[idx]
    return res

url = ""https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a""
rs = cutstr(url, "/", 3)
print(rs) """


""" import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutstr(url, "/", 3)
print(res) """


#내장모듈 모듈

# math
""" import math

sq_res = math.sqrt(6)
print(sq_res)

sq_res = math.sin(math.pi / 2)
print(sq_res)

e_res = math.log(math.e)
print(e_res)

exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)

fc_res = math.factorial(4)
print(fc_res) """

""" import mod.utils as mu

res = mu.mt_sqrt(7)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog()
print(el)

ep = mu.mt_exp(3)
print(ep)

pi = mu.mt_pi()
print(pi) """


""" import random as rd

res = rd.randint(1, 100)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.random()
print(fres)

nvres = rd.normalvariate()
print(nvres) """

# 모듈화 
""" import mod.utils as mu

my_list = ['apple', 'banana', 'cherry']
print(mu.rd_int(1, 100))
print(mu.rd_list(my_list))
print(mu.rd_rd())
print(mu.rd_nmvar()) """

""" #datetime 이용 함수 

from datetime import datetime as dt

# 현재시간 출력
print(dt.now())

# 특정시간대의 현재 시간 출력
from pytz import timezone
#tz = timezone('Asia/Seoul')
tz = timezone('UTC')
print("timezone : ", dt.now(tz))

# 문자열을 날짜로 변환
date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y - %m - %d')
print(date_object)

# 날짜를 문자열로 변환 
date_object = dt.now()
date_string = date_object.strftime('%Y - %m - %d')
print(date_string) """

""" import mod.utils as mu
dtnow = mu.get_dtnow()
print(dtnow())

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time() 
print(res)
"""

# os 모듈 확인

"""import os """

"""
# 현재 작업 디렉토리 출력 
print(os.getcwd())

# 디렉토리 변경
os.chdir('../')

# 변경된 디렉토리 출력
print(os.getcwd())

# 파일 목록 출력
print(os.listdir())

# 디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())

# 디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir()) """

""" import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python1"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir()) """

""" import sys

# 버전 정보 출력
print(sys.version)

# 명령 인수 확인
print(sys.argv)
 """
 
 
 # 파이썬으로 스택 구성하기
 
 # 스택
""" list = []

# 스택
list.append(1)
list.append(2)
list.append(3) 
list.append(4) 
list.append(5) 

#스택의 상태 확인
print(list)

 #스택에서 값 빼기
top = list.pop
print(top)
print(list)
print(len(list))  """
 

# 큐 

""" queque = []

queque.append(1)
queque.append(2)
queque.append(3)
queque.append(4)
queque.append(5)


print(queque)

front = queque.pop(0)
print(front)
print(queque)
print(len(queque)) """

""" qlist = []

def enqueue(qlist, data):
    qlist.append(data)
    
def dequeue(qlist):
    data = qlist[0]
    del qlist[0]
    return data

enqueue(qlist, 1)
print(qlist)

enqueue(qlist, 2)
print(qlist)

enqueue(qlist, 3)
print(qlist)

dequeue(qlist)
print(qlist)

dequeue(qlist)
print(qlist) """


""" import time """

""" arr = [1, 2, 3, 4, 5]

def ret_01(idx):
    return arr[idx]

start = time.time()
print(ret_01(2))
end = time.time()
print(f"{end - start : 5f} sec") """

""" arr = [1, 2, 3, 4, 5]

def print_elements(arr):
    for elem in arr:
        print(elem)

start = time.time()
print_elements(arr)
end = time.time()

print(f"{end - start : 5f} sec")
 """
""" import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

my_list = [1, 2, 3, 4, 5]

result = binary_search(my_list, 4)
if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.")
 """

import time
def mul_for():
    for i in range(5):
        for j in range(5):
            print(i, j)
            
start = time.time()
mul_for()
end = time.time()
print(f"{end - start : 5f} sec") 



































