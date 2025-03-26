from itertools import combinations

#실제 작성한 코드
def solution(number):
    answer = 0
    
    result = list(combinations(number, 3))
    
    for eachNum in result:
        if eachNum[0] + eachNum[1] + eachNum[2] == 0:
            answer += 1
            
    
    return answer

#개선된 코드
#기존 리스트 제거 list(combinations())같은것들
def solution2(number):
    
    answer = 0
    answer = sum( 1 for ele in combinations(number, 3) if sum(ele) == 0)    
    
    return answer

# number = [-3,-2,-1,0,1,2,3]
number = [-2, 3, 0, 2, -5]
answer = solution2(number)
print(answer)