import heapq

#실제 작성한 코드
def solution(d, budget):
    
    answer = 0
    arr = []
    
    for i in d:
        heapq.heappush(arr, i)
        
    for j in range(len(arr)):
        minNum = heapq.heappop(arr)
        if budget >= minNum:
            answer += 1
            budget -= minNum
        else:
            break
    
    return answer

# 개선된 코드
def solution2(d, budget):
    
    heapq.heapify(d)
    
    answer = 0
    while d and budget >= d[0]:
        budget -= heapq.heappop(d)
        answer += 1
    
    return answer

d = [1,3,2,5,4]
budget = 9
answer = solution2(d, budget)
print(answer)