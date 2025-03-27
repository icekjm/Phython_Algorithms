
#초기 작성한코드
def solution1(sizes):
    answer = 0
    bigArr = []
    smallArr = []
    
    for i in sizes:
        bigArr.append(max(i))
        smallArr.append(min(i))
    
    width = max(bigArr)
    height = max(smallArr)
    
    answer = width * height
    
    return answer

#실제 작성한 코드
def solution2(sizes):
    answer = 0
    
    maxArr = [ max(eachArr) for eachArr in sizes]
    minArr = [ min(eachArr) for eachArr in sizes]
    
    maxWidth = max(maxArr)
    maxheight = max(minArr)
    answer = maxWidth * maxheight
    
    return answer

#개선된코드1
def solution3(sizes):
    answer = 0

    arr = [(max(eachArr), min(eachArr)) for eachArr in sizes]
    width, height = zip(*arr)
    answer = max(width) * max(height)
    
    return answer

#개선된코드 2
def solution4(sizes):
   width, height = zip(*[(max(eachArr), min(eachArr)) for eachArr in sizes])
   return max(width) * max(height)

sizes = [[60, 50],[30, 70],[60, 30],[80, 40]]
answer = solution3(sizes)
print(answer)