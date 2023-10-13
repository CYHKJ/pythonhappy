""" from datetime import datetime as dt

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
print(date_object) """

# 날짜를 문자열로 변환 
"""date_object = dt.now()
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

queque = []

queque.append(1)
queque.append(2)
queque.append(3)
queque.append(4)
queque.append(5)


print(queque)

front = queque.pop(0)
print(front)
print(queque)
print(len(queque)) 
