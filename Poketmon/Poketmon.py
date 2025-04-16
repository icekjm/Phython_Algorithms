from itertools import groupby

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

# nums = [3,1,2,3]
nums = [3,3,3,2,2,4]
# nums = [3,3,3,2,2,2]

answer = solution(nums)
print(answer)