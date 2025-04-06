import heapq
import time
#실제작성한코드
def solution(k, score):
    answer = []
    topTeer = []
    st_time = time.time()
    for indiScore in score:
        if not topTeer or len(topTeer) < k:
            topTeer.append(indiScore)
            topTeer.sort(reverse=True)
            answer.append(topTeer[-1])
        else:
            if indiScore > topTeer[-1]:
                topTeer[-1] = indiScore
                topTeer.sort(reverse=True)
                answer.append(topTeer[-1])
            else:
                answer.append(topTeer[-1])
    ed_time = time.time()
    print("소요시간 : ", ed_time - st_time)            
        
    return answer

#코드개선
def solution2(k, score):
    st_time = time.time()
    answer = []
    topTeer = []
    
    for each in score:
        heapq.heappush(topTeer, each)
        if len(topTeer) > k:
            heapq.heappop(topTeer)
        answer.append(topTeer[0])
    
    ed_time = time.time()
    print("소요시간 : ", ed_time - st_time)    
    
    return answer

# score = [10, 100, 20, 150, 1, 100, 200]
# k = 3
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
k = 4
answer = solution(k, score)
print(answer)