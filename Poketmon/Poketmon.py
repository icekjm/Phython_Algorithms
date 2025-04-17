from itertools import groupby

#실제 작성한 코드
def solution(nums):
    answer = 0
    keyArr = []
    
    nums.sort()
    grouped = groupby(nums)
    
    for key in grouped:
        keyArr.append(key[0])
    
    maxNum = len(nums) // 2

    if len(keyArr) >= maxNum:
        answer = maxNum
    else:
        answer = len(keyArr)
    
    return answer

nums = [3,1,2,3]
# nums = [3,3,3,2,2,4]
# nums = [3,3,3,2,2,2]

#개선된 코드
def solution2(nums):
    answer = 0
    
    answer = min(len(nums) // 2, len(set(nums)))
    
    return answer

answer = solution2(nums)
print(answer)