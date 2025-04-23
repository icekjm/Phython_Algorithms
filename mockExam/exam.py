
#실제 작성한 코드1(시간초과로 인한 실패)
def solution(answers):
    answer = []
    rank = dict()
    
    #총문항수
    total = len(answers)
    
    answerA, answerB, answerC = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5] 
    repNo_A, repNo_B, repNo_C = len(answers) // len(answerA), len(answers) // len(answerB), len(answers) // len(answerC)
    
    scoreA, scoreB, scoreC = 0, 0, 0
    
    #A답안지 작성
    if total >= len(answerA):
        for _ in range(1, repNo_A):
            answerA.extend(answerA)
        answerA.extend(answerA[: total % len(answerA) ])
    
    #B답안지 작성
    if total >= len(answerB):
        for _ in range(1, repNo_B):
            answerB.extend(answerB)
        answerB.extend(answerB[: total % len(answerB) ])
    #C답안지 작성
    if total >= len(answerC):
        for _ in range(1, repNo_C):
            answerC.extend(answerC)
        answerC.extend(answerC[: total % len(answerC) ])
    #A,B,C 답안지
    for i in range(0, total):
        if answerA[i] == answers[i]:
            scoreA += 1
        if answerB[i] == answers[i]:
            scoreB += 1
        if answerC[i] == answers[i]:
            scoreC += 1        
    
    rank[1], rank[2], rank[3] = scoreA, scoreB, scoreC
    
    maxScore = rank[max(rank, key=rank.get)] 
    answer = [ i for i, v in rank.items() if v == maxScore]
        
    return answer

#실제 작성한 코드1의 실패 원인: 

#실제작성한코드2 개정(아래 코드는 Runtime 에러)
def solution2(answers):
    answer = []
    rank = dict()
    
    #총문항수
    total = len(answers)
    
    answerA, answerB, answerC = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5] 
    repNo_A, repNo_B, repNo_C = total // len(answerA), total // len(answerB), total // len(answerC)
    
    scoreA, scoreB, scoreC = 0, 0, 0
    
    #A답안지 작성
    if total > len(answerA):
        answerA = (answerA * ( repNo_A )).extend(answerA[: total % len(answerA)])
    
    #B답안지 작성
    if total > len(answerB):
        answerB = (answerB * (repNo_B)).extend(answerB[: total % len(answerB)])
    
    #C답안지 작성
    if total > len(answerC):
        answerC = (answerC * (repNo_C)).extend(answerC[: total % len(answerC)])
    
    #A, B, C 채점시작
    for i in range(0 , total):
        if answerA[i] == answers[i]:
            scoreA += 1
        if answerB[i] == answers[i]:
            scoreB += 1
        if answerC[i] == answers[i]:
            scoreC += 1
    
    rank[1], rank[2], rank[3] = scoreA, scoreB, scoreC        
    
    maxScore = rank[max(rank, key=rank.get)]
    answer = [ i for i, eachScore in rank.items() if eachScore == maxScore]
        
    return answer

#실제 작성한 코드2의 실패 원인:

#실제작성한코드2 최종개정
def solution2(answers):
    answer = []
    rank = dict()
    
    #총문항수
    total = len(answers)
    
    answerA, answerB, answerC = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5] 
    repNo_A, repNo_B, repNo_C = total // len(answerA), total // len(answerB), total // len(answerC)
    
    scoreA, scoreB, scoreC = 0, 0, 0
    
    #A답안지 작성
    if total > len(answerA):
        answerA = (answerA * ( repNo_A + 1 ))[:total]
    
    #B답안지 작성
    if total > len(answerB):
        answerB = (answerB * (repNo_B + 1))[:total]
    
    #C답안지 작성
    if total > len(answerC):
        answerC = (answerC * (repNo_C + 1))[:total]
    
    #A, B, C 채점시작
    for i in range(0 , total):
        if answerA[i] == answers[i]:
            scoreA += 1
        if answerB[i] == answers[i]:
            scoreB += 1
        if answerC[i] == answers[i]:
            scoreC += 1
    
    rank[1], rank[2], rank[3] = scoreA, scoreB, scoreC        
    
    maxScore = rank[max(rank, key=rank.get)]
    answer = [ i for i, eachScore in rank.items() if eachScore == maxScore]
        
    return answer

# answers = [1,2,3,4,5,2,1,2,3,4,2,5] 
# answers = [1,2,3,4,5]
answers = [1,3,2,4,2]

answer = solution2(answers)
print(answer)

