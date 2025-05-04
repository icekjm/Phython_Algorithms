from itertools import combinations
import math

#실제작성한코드
def solution(nums):
    answer = 0

    for each in combinations(nums, 3):
        eachSum = sum(each)
        cnt = 0
        for i in range(1, eachSum+1):
            if eachSum % i == 0:
                cnt += 1
        
        if cnt == 2:
            answer += 1

    return answer

#개선코드
def solution2(nums):
    answer = 0
    
    for each in combinations(nums, 3):
        if isItPrime(sum(each)):
            answer += 1
    
    return answer

def isItPrime(number):
    if number < 2:
        return False
    else:
        for indiNum in range(2, int(math.sqrt(number))+1):
            if number % indiNum == 0:
                return False
        return True
    

# nums = [1,2,3,4]
nums = [1,2,7,6,4]
answer = solution2(nums)
print(answer)