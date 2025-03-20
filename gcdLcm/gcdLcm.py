import math

#실제 작성한 코드
def solution(n, m):
    answer = []
    
    greatCmm = math.gcd(n, m)
    answer.append(greatCmm)
    lcm = (n // greatCmm) * (m // greatCmm) * greatCmm
    answer.append(lcm)
    
    return answer

#개선된 코드
def solution2(n, m):
    answer = []
    
    gcd_val = math.gcd(n, m)
    lcm_val = (n * m) // gcd_val
    
    return [gcd_val, lcm_val]


n, m = 6, 8
answer = solution2(n, m)
print(answer)