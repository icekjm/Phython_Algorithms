#실제작성한 코드
def solution(n):
    answer = 0
    
    numDivisor = [0] * (n+1)
    
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            numDivisor[j] += 1
    
    answer = sum(1 for eachVal in numDivisor if eachVal == 2)
    
    return answer

#개선된 코드
def solution2(n):
    answer = 0
    
    numDivisor = [True] * (n+1)
    numDivisor[0], numDivisor[1] = False, False
    
    for i in range(2, int(n ** 0.5) + 1):
        if numDivisor[i]:
            for j in range(i*i, n+1, i):
                numDivisor[j] = False

    answer = sum(numDivisor)

    return answer


# n = 10
n = 5

answer = solution2(n)
print(answer)