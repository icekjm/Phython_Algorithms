from collections import deque

#실제 작성한 코드
def solution(cards1, cards2, goal):
    answer = ''
    queCds1 = deque(cards1)
    queCds2 = deque(cards2)
    queGoal = deque(goal)
    count = 0
    
    while len(queGoal) > 0:
        tarGwd = queGoal.popleft()
        if len(queCds1) > 0 and queCds1[0] == tarGwd:
            queCds1.popleft()
            count += 1
        if len(queCds2) > 0 and queCds2[0] == tarGwd:
            queCds2.popleft()
            count += 1
    
    if count == len(goal):
        answer = 'Yes'
    else:
        answer = 'No'
    
    return answer

#개선된 코드
def solution2(cards1, cards2, goal):
    answer = ''
    
    queCds1 = deque(cards1)
    queCds2 = deque(cards2)
    
    for each in goal:
        if queCds1 and queCds1[0] == each:
            queCds1.popleft()
        elif queCds2 and queCds2[0] == each:
            queCds2.popleft()
        else:
            answer = "No"
    
    if not answer:
        answer = "Yes"
    
    return answer



cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

# cards1 = ["i", "water", "drink"]
# cards2 = ["want", "to"]
# goal = ["i", "want", "to", "drink", "water"]

answer = solution2(cards1, cards2, goal)
print(answer)