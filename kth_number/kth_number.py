#실제로 작성한 코드
def solution(array, commands):
    answer = []
    
    answer = [ sorted(array[eachArr[0]-1:eachArr[1]])[eachArr[2]-1]
        for eachArr in commands
    ]
    
    return answer
#코드개선1
def solution2(array, commands):
    
    answer = []
    
    answer = [
        sorted(array[i-1:j])[k-1]
        for i, j, k in commands
    ]
    
    return answer

#lambda + map버전
#아래 코드는 오답 map()은 하나씩만 lambda에 전달하는데, i,j,k를 풀어서 전달하지 않음(위 코드개선1참조)
# def solution3(array, commands):
#     return list(map(lambda i,j,k:sorted(array[i-1:j])[k-1] ,commands))
def solution3(array, commands):
    return list(map(lambda eachArr: sorted(array[eachArr[0]-1:eachArr[1]])[eachArr[2]-1],commands))

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = solution3(array, commands)
print(answer)