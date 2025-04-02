def solution(a, b, n):
    answer = 0
    
    while n // a > 0:
        if n % a == 0:
            answer += n // a
        else:
            answer += (n // a)
            n = (n // a) + (n % a)
    
    return answer

a, b = 2, 1
n = 20
# a, b = 3, 1
# n = 20
answer = solution(a,b,n)
print(answer)