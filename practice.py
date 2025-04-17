# 파이썬에서 전역변수와 지역변수의 쓰임
#CASE1
a = 10	
    
def prac():
    print(a)
    
print(a)
prac()

#CASE2
a = 10
    
def prac2():
    a = 5
    a += 10
    print(a)
        
print(a)
prac2()
# #다시 a실행
print(a)
    
#CASE3
a = 10
    
def prac2():
    global a
    a += 10
    print(a)
        
print(a)
prac2()    
#다시 a실행
print(a)    