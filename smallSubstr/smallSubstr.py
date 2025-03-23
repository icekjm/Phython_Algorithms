
#실제 작성한 코드
def solution(t, p):
    
    answer=0
    
    for i in range(len(t)-len(p)+1):
        rdNum = t[i : i + len(p)]
        if int(rdNum) <= int(p):
            answer += 1
    
    return answer

#개선된 코드
def solution2(t, p):

    pNum = int(p)
    return sum( 1 for i in range(len(t) - len(p) + 1) if int(t[i:i+len(p)]) <= pNum)

t="10203"
p="15"
answer = solution2(t, p)
print(answer)