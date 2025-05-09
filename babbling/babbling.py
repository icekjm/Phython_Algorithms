import re

def solution(babbling):
    answer = 0
    pattern = re.compile(r'^(?!.*(aya|ye|woo|ma)\1)(aya|ye|woo|ma)+$')
    answer = sum(bool(pattern.fullmatch(eachWord)) for eachWord in babbling)
    
    return answer


babbling = ["aya", "yee", "u", "maa"]
# babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

answer = solution(babbling)
print(answer)