#실제 작성한 코드
def solution(wallet, bill):
    answer = 0
    
    walMax = max(wallet)
    walMin = min(wallet)
    
    while max(bill) > walMax or min(bill) > walMin:
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
            answer += 1
        else:
            bill[1] = bill[1] // 2
            answer += 1
        if walMax >= max(bill) and walMin >= min(bill):
            break
        
    return answer

# wallet, bill = [30, 15], [26, 17]
wallet, bill = [50, 50], [100, 241]

answer = solution(wallet,bill)
print(answer)

