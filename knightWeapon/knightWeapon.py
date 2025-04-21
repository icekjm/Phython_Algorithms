
#실제 작성한 미달코드 1
def solution1(number, limit, power):
    answer = 0
    attackArr = []
    
    for personNo in range(1, number + 1):
        cnt = 0
        for eachNo in range(1, personNo + 1):
            if personNo % eachNo == 0:
                cnt += 1
        
        if cnt > limit:
            attackArr.append(power)
        else:
            attackArr.append(cnt)
    
    answer = sum(attackArr)    
        
    return answer

#실제 작성한 미달코드 2
def solution2(number, limit, power):
    answer = 0
    
    for personNo in range(1, number + 1):
        cnt = 0
        for eachNo in range(1, personNo + 1):
            if personNo % eachNo == 0:
                cnt += 1
        
        if cnt > limit:
            answer += power
        else:
            answer += cnt  
    return answer

#실제 작성한 미달코드 3
def solution3(number, limit, power):
    answer = 0
    
    for personNo in range(1, number + 1):
        cnt = 0
        #짝수일때
        if personNo % 2 == 0:
            for each in range(1, personNo+1):
                if personNo % each == 0:
                    cnt += 1
        else: #홀수일때
            for each in range(1, personNo+1, 2):
                if personNo % each == 0:
                    cnt +=1
        
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    
    return answer

#미달코드의 공통점: number의 크기가 100,000일 경우 이중 for문 사용시 50억번을 연산을 진행

#에라토스테네스의 체를 응용한 코드 구현
#아래 코드 이용시 130만번~ 300만으로 연산횟수가 줄어듦
def solution4(number, limit, power):
    answer = 0
    
    attkArr = [0] * number
    
    for person in range(1, number+1):
        for divinder in range(person, number+1, person):
            attkArr[divinder-1] += 1
        if attkArr[person - 1] > limit:
            attkArr[person - 1] = power
    
    print(attkArr)
    answer = sum(attkArr)
        
    return answer

#직관적이해: number=10인 경우, 이중 for문을 이용한 연산횟수는 55번정도!
#하지만 위 에라토스테네스를 응용한 방식은 연산횟수가 27번! -> number가 커질수록 연산횟수는 기하급수적으로 감소함

# number = 5
# limit = 3
# power = 2
number = 10
limit = 3
power = 2

answer = solution3(number, limit, power)
print(answer)
