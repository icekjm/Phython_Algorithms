import re

#실제 작성한 코드
def solution1(s):
    answer = '' 
    mArr = []
    
    for ele in re.findall(r'\s+|\S+', s):
        if ele.isspace():
            mArr.append(ele)
        else:
            word = ''
            for i in range(0, len(ele)):
                if i % 2 == 0:
                    word += ele[i].upper()
                else: 
                    word += ele[i].lower()
            mArr.append(word)    
    
    answer = ''.join(mArr)

#개선코드1
def solution2(s):
    answer = ""
    
    strArr = re.findall(r'\s+|\S+', s)
    answerArr = [ eachWord
        if eachWord.isspace() else 
        "".join( value.upper() if i % 2 == 0 else value.lower() for i, value in enumerate(eachWord))
        for eachWord in strArr
    ]
    
    answer = "".join(answerArr)
    
    return answer

#개선코드2
def solution3(s):
    answer = '' 
    mArr = []
    
    #리스트내포문을 이용할경우!
    #[출력식1 if 조건1 else (출력식2 if 조건2 else 출력식3) for 변수 in 리스트]
    mArr = [
        ele if ele.isspace() 
        else "".join(
            value.upper() if index % 2 == 0 else value.lower()
            for index, value in enumerate(ele)
        )
        for ele in re.findall(r'\s+|\S+', s)
    ]
    
    answer = ''.join(mArr)
    
    return answer

s = "try hello world"
j = "   hello   jimin"
answer = solution3(j)
print(answer)