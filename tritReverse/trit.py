
# 실제 작성한 코드
def solution(n):
    answer = 0
    remain = ""
    
    if n >= 3:
        while n // 3 != 0:
           remain += str(n % 3)
           n = n // 3
           if n < 3:
               remain += str(n)        
    else:
        remain = str(n)
    
    for i in range(len(remain)):
        answer += int(remain[i]) * ( 3 **( int(len(remain)) - 1 - i ) )
    
    return answer

# 개선된 코드
def solution2(n):
    
    answer = 0
    remainArr = []
    
    while n > 0:
        remainArr.append(n % 3)
        n = n // 3
    
    answer = sum( val * (3**i)  for i, val in enumerate(remainArr[::-1]))    
        
    return answer

n = 45
answer = solution2(n)
print(answer) 

   