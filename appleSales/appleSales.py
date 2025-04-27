import heapq

#실제 작성한 코드
#문제점: 해당 문제에서 요구하는 k 파라미터를 이용하지 않았음.
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

#다시 작성한 코드: 카운팅정렬을 이용한 풀이
def solution2(k, m, score):
    answer = 0
    eachBox = []
    
    cntSort = [0] * (k+1)
    
    for each in score:
        cntSort[each] += 1
    
    for i in range(k, 0, -1):
        for _ in range(cntSort[i]):
            if len(eachBox) < m:
                eachBox.append(i)
            
            if len(eachBox) == m:
                sales = min(eachBox) * m
                answer += sales
                eachBox = []
    
    return answer

def solution3(k, m, score):
    answer = 0
    
    cntSort = [0] * (k+1)
    
    for eachScore in score:
        cntSort[eachScore] += 1
    
    eachBox = 0
    for index in range(k, 0, -1):
        eachBox += cntSort[index]
        
        while eachBox >= m:
            answer += (m * index)
            eachBox -= m
    
    return answer

# k, m = 3, 4
# score = [1, 2, 3, 1, 2, 3, 1]
k, m = 4, 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
answer = solution3(k, m, score)
print(answer)