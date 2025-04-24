import heapq

def solution(k, m, score):
    answer = 0
    cmpAppleTree = []
    
    boxNums = len(score) // m
    
    for eachApple in score:
        heapq.heappush(cmpAppleTree, -eachApple)
    
    for _ in range(0, boxNums):
        eachBox = [ -heapq.heappop(cmpAppleTree) for _ in range(0, m) if len(cmpAppleTree) > 0 ]
        sales = min(eachBox) * m
        answer += sales
    
    return answer





















# k, m = 3, 4
# score = [1, 2, 3, 1, 2, 3, 1]
k, m = 4, 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
solution(k, m, score)