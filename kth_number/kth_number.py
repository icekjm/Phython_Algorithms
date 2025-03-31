def solution(array, commands):
    answer = []
    
    answer = [ sorted(array[eachArr[0]-1:eachArr[1]])[eachArr[2]-1]
        for eachArr in commands
    ]
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = solution(array, commands)
print(answer)