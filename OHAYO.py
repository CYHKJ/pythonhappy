""" my_list = [9, 4, 3, 7, 8, 'hi']
print(4 in my_list)
print(2 in my_list)
print(2 not in my_list) """

""" my_dic = {"key1" : "v1", "k2" : "v2"}
print("k2" in my_dic) """

""" x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  
print(x is z)  
print(x is not y)   """

""" a = 5
b = 5
print(a is b)
print(a is not b) """

""" print(3 == 3.0)
print(3 is 3.0) """

""" a = [3, 5, 1]
b = a
print(a is b)
print(a is not b)

a[0] = 2
print(a, b)
print(a is b) """

""" x = 2 ** 3 ** 2
print(x) """  

""" x = 2 + 3 * 4 
print(x) """

""" x =10 / 5 / 2
print(x) """

""" x = 2 ** 3 ** 2
print(x) """

""" x = 10 % 3 % 2
print(x) """

""" x = 1 + 2 > 3 and 4 - 1 < 2
print(x) """


""" x = not False and True
print (x)
 """

""" x = not True or False and True
print(x) """

""" x = 1 * 2 | 3 ^ 4
print(x) """

""" x = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
print(x) """

""" x = 2 * -3 // 2
print(x) """

""" x = 1 == 2
print(x) """

""" x = False != 3
print(x) """

""" x = 10
    x = -1
    x = 0
    
if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero") """

""" x = 10
if x % 2 == 0:
    print("x 는 짝수다")
elif x % 2 != 0:
    print("x는 홀수다") """
    
""" x = 10 
y = 15
if x == y:
    print("같다")
elif x != y:
    print("다르다") """
    
""" x = 'a'
if x == 'a':
    print("a이다")
elif x == 'b':
    print("b이다")    """
    
""" fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit) """
    
""" my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)    """
    
""" my_list = [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in my_list:    
    for num in row:
        print(num)   """
    
""" my_list = "happy"
for munja in my_list:
    print(munja) """

""" fruits = ["apple", "banana", "cherry"]
fruits.reverse()
for row in fruits:
    print(row) """

""" fruits = ["apple", "banana", "cherry"]
for fruit in sorted(fruits, reverse = true):
    print(row) """

""" for x in range(2,10): 
    for y in range(1,10):
        print(x, '*', y, '=', x * y) """

""" rang = [5, 8, 3, 1, 6]
for i in rang:
	print("element : ", i)
else :
	print("end process") """
 
""" for i in range(10):
    if i == 7:
        break
    elif i == 1:
        continue
    else:
        pass

    print(i)
 """

#while문
""" i = 1
while i <= 5:
    print(i)
    i += 1 """

# 0부터 9까지 출력 (while)
""" i = 0
while i <= 9:
    print(i)
    i += 1 """

# 문자열을 한글자씩 출력 (while)    
""" str_word = "happy"
idx = 0 
while idx < len(str_word):
    print(str_word[idx])
    idx += 1 """
    
# 1부터 10까지 총합 출력 (while)   
""" sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
    print(sum) """

# 1에서 100까지의 짝수 (while) 
i = 1
while i <= 100:
    if i % 2 == 0:
        print("짝수 : ", i)
    elif i % 2 == 1:
        print("홀수 : ", i)
    i+=1

""" i = 1

while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1 """
    







