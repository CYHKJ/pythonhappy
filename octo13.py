# 삼각형 출력
# 직각삼각형
""" for i in range(1, 6):
    print("*" * i) """
    
# 역직각삼각형   
""" for i in range(5, 0, -1):
	print("*" * i)  """
 
# 이등변 삼각형
""" for i in range(1, 6):
    spases = " " * (6 - i)
    stars = "*" * (2*i-1)
    print(spases + stars) 

for i in range(6, 0, -1):
    spases = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spases + stars) """

# 5X5 출력
""" num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """

# 세로로 출력
""" line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j-1) * 5) + i
        line.append(num)
    print(line)
    line = [] """

#역순출
""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = [] """


# 가위바위보 게임
""" import random

def get_computer_choice():
    choices = ['1', '2', '3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("무승부")
        return
    elif (
        (user_choice == '1' and pcnum == '3')or
        (user_choice == '2' and pcnum == '1')or
        (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print("패")  
        return  
    
print("1 : 가위")    
print("2 : 바위") 
print("3 : 보") 
print("1~3 숫자를 입력하세요") 
chnum = input()

determine_winner(chnum) """


# 파일 처리

""" file = open("temp.txt", "w")
file.close() """


""" file = open("temp.txt", "r")
file.close() """


""" file = open("temp.txt", "a")
file.close() """


""" file = open("temp.txt", "r+")
file.close() """


""" file = open("temp.txt", "w")

file.write("hello\n")
file.write("world")

file.close() """


""" file = open("temp.txt", "w")

for i in  range(1, 101):
    file.write(f"{i}\n")
file.close()  """ 

""" f = open("C:\\Users\\Catholic\\temp.txt", "w")

for i in  range(1, 101):
    f.write(f"{i}\n")
f.close() 


f = open("C:\\Users\\Catholic\\temp.txt", "a")
f.write("hello\n")
f.write("world")
f.close() """

# 파일 읽기
""" file = open("temp.txt", "r")
res = file.read()
print(res)

file.close() """

# 다른경로 파일 읽기

""" file = open("C:\\Users\\Catholic\\temp.txt", "r")
res = file.read()
print(res)

file.close() """

# readline

""" file = open("temp.txt", "r")
for i in range(110):
    res = file.readline()
    print(res)

file.close() """ 

# readlines


""" file = open("temp.txt", "r")
res = file.readlines()
print(res)

file.close()   """  


""" f = open("temp.txt", "r")
line = f.readlines()
for l in line:
    print(l)
    
f.close()   """  

# file object

f = open("temp.txt", "r")
for line in f:
    print(line)
    
f.close()    


""" import os

fp = "temp.txt"
#fp = "temp1.txt"

if os.path.exists(fp) :
	print("ok")
else :
	print("error") """


















