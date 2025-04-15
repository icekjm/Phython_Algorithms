#실제작성한 코드
def solution(name, yearninig, photo):
    answer = []
    
    for eachPhoto in photo:
        photoSum = sum(yearning[name.index(person)] for person in eachPhoto if person in name )
        answer.append(photoSum)
    
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

answer = solution(name, yearning, photo)
print(answer)