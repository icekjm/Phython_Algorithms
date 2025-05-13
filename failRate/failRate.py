def solution(N, stages):
    answer = []
    
    stageCntArr = [0] * (N + 2)
    
    for eachStg in stages:
        stageCntArr[eachStg] += 1
    
    answer = createDict(stageCntArr, N)
    
    return answer

def createDict(arrStage, N):
    failDict = dict()
    totalPeople = sum(arrStage) 
    
    for eachStp in range(1, N+1):
        totalPeople -= arrStage[eachStp - 1]
        if totalPeople == 0:
            failDict[eachStp] = 0
        else:
            failDict[eachStp] = arrStage[eachStp] / totalPeople
    
    sortedDict = sorted(failDict.items(), key=lambda x: (-x[1], x[0]))
    
    return [ each[0] for each in sortedDict]
    
    
    
    






# N, stages = 5, [2, 1, 2, 6, 2, 4, 3, 3]
N, stages = 4, [4, 4, 4, 4, 4]
answer = solution(N, stages)
print(answer)