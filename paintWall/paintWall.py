#실제작성한 코드
def solution(n, m, section):
    answer = 1
    
    end = section[0] + m - 1 
        
    for each in section:
        if end < each:
            answer += 1
            end = each + m - 1
            if end > n :
                break        
    
    return answer


# n, m = 8, 4
# section = [2, 3, 6]
# n, m = 5, 4
# section = [1, 3]
n, m = 4, 1
section = 1, 2, 3, 4

answer = solution(n, m, section)
print(answer)
