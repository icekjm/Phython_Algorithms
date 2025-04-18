import datetime

#실제작성한코드
def solution(a, b):
    answer = ''
    
    dictWeek = {
        0: "MON",
        1: "TUE",
        2: "WED",
        3: "THU",
        4: "FRI",
        5: "SAT",
        6: "SUN"
    }
    
    tempDate = datetime.date(2016, a, b)
    dayOfWeek = tempDate.weekday()
    answer = dictWeek[dayOfWeek]
    
    return answer

a = 5
b = 24

answer = solution(a, b)
print(answer)