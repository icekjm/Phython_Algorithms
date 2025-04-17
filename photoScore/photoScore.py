#실제작성한 코드
def solution(name, yearninig, photo):
    answer = []
    
    for eachPhoto in photo:
        photoSum = sum(yearning[name.index(person)] for person in eachPhoto if person in name )
        answer.append(photoSum)
    
    return answer


#개선된 코드
def solution2(name, yearning, photo):
    answer = []
    
    score_map = dict(zip(name, yearning))
    
    # for eachPhoto in photo:
    #     answer.append( sum( score_map.get(person, 0) for person in eachPhoto ) )
    
    answer = [sum(score_map.get(person, 0) for person in each_photo) for each_photo in photo]
    
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

answer = solution2(name, yearning, photo)
print(answer)