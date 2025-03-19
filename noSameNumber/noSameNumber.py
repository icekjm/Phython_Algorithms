from collections import deque
from itertools import groupby

#실제 작성한 코드드
def solution(arr):
    answer = []
    numArr = deque(arr)
    
    for i in range(0, len(arr)):
        if len(answer) == 0:
            answer.append( numArr.popleft() )    
        else:
            lastEle = numArr.popleft()
            if answer[-1] == lastEle:
                continue
            else:
                answer.append(lastEle)
    
    
    return answer

#개선코드1
def solution1(arr):
    
    grouped = groupby(arr)
    
    answer = [ key for key, group in grouped]
        
    return answer

#개선코드2
def solution2(arr):
    
    answer = []
    
    for each in arr:
        if not answer or answer[-1] != each:
            answer.append(each)
        
    return answer

arr = [4,4,4,3,3]
answer = solution2(arr)
print(answer)
