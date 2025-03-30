#딕셔너리를 이용할 경우
from collections import defaultdict

def solution(strings, n):
    answer = []
    
    #키의 기본값이 리스트가 되도록 설정
    groupedDict = defaultdict(list)
    #키의 값이 같은것끼리 그룹화 하여 리스트에 추가
    for each1 in strings:
        groupedDict[each1[n]].append(each1)
    #각 키 내부의 리스트를 오름차순 정렬
    for key in groupedDict:
        groupedDict[key].sort()
    #키를 오름차순으로 정렬하고 answer 배열에 추가
    for key in sorted(groupedDict):
        answer.extend( groupedDict[key] )
    
    return answer

#개선된코드
def solution2(strings, n):
    return sorted(strings, key=lambda x:(x[0], x))

# strings = ["sun", "bed", "car"]
# n = 1
strings = ["abcd", "abce", "cdx"]
n = 2
answer = solution2(strings, n)
print(answer)