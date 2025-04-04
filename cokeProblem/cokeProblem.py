#실제 작성한코드
def solution(a, b, n):
    answer = 0
    numCoke = 0
    
    while n // a > 0:
        numCoke = (n // a) * b
        answer += numCoke
        if n % a == 0:   
            n = numCoke
        else:
            n = (n // a) * b + (n % a)
    
    return answer

#개선된코드
def solution2(a,b,n):
    
    answer = 0
    
    while n > a:
        exchanged = (n // a) * b
        answer += exchanged
        n = exchanged + (n % a)
    
    return answer

# a, b = 2, 1
# n = 20
a, b = 3, 1
n = 20
answer = solution(a,b,n)
print(answer)