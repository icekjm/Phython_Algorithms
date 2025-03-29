import time

#실제작성한코드1
def solution(s):
    answer = 0
    
    #시간측정
    st_time = time.time()
    
    numArr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    if s.isdigit() == False:
        for index, val in enumerate(numArr):
            s = s.replace(val, str(index))
    
    answer = int(s)
    
    ed_time = time.time()
    print("시간측정 : ", ed_time - st_time)
    
    return answer

#실제 작성한 코드2
def solution2(s):
    answer = 0
    
    dicArr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for num, alpha in enumerate(dicArr):
        s = s.replace(alpha, str(num))
    
    answer = int(s)    
    
    return answer

#개선코드
def solution3(s):
    answer = 0
    st_time = time.time()
    
    dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    for key, value in dict.items():
        s = s.replace(key, value)
    
    answer = int(s)
    
    ed_time = time.time()
    print("시간측정 : ", ed_time - st_time)    
    
    return answer

s="one4seveneight"
# s="1478"
answer = solution3(s)
print(answer)