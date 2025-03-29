import time

#실제작성한코드1
def solution(food):
    answer = ''
    
    st_time = time.time()
    
    eachArr = [
        str(i) for i, v in enumerate(food) if v > 1
        for k in range(v // 2)
    ]
    #sorted 함수에서 배열이 안의 원소가 숫자든 문자열이든 상관없이 정렬시켜줌
    otherArr = sorted(eachArr, reverse = True)
    answer = "".join(eachArr) + "0" + "".join(otherArr) 
    
    ed_time = time.time()
    print("실제 소요된 시간 : ", ed_time - st_time)
    
    return answer

#실제작성한코드2
def solution2(food):
    answer = ''
    
    st_time = time.time()
    
    readyArr = [ str(num)
                for num, fdName in enumerate(food)
                if fdName // 2 > 0
                for _ in range(fdName // 2)
                ]
    
    answer = "".join(readyArr) + "0" + "".join(readyArr[::-1])
    
    ed_time = time.time()
    print("실제 소요된 시간 : ", ed_time - st_time)
    
    return answer

#개선된 코드
def solution3(food):
    # 리스트 내포 순서 조정하여 더 직관적인 코드로 변경
    eachArr = [str(i) for i, v in enumerate(food) for _ in range(v // 2)]
    
    # 뒤집을 때 sorted() 대신 슬라이싱을 사용하여 성능 향상
    answer = "".join(eachArr) + "0" + "".join(eachArr[::-1])
    
    return answer

food = [1, 3, 4, 6]
answer = solution2(food)
print(answer)