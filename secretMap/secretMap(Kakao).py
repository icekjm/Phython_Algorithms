
#실제 작성한 코드
def solution(n, arr1, arr2):
    
    answer = []
    map1 = []
    map2 = []
    
    #map1
    for eachNum in arr1:
        strBinary = ""
        for _ in range(n):
            strBinary = str(eachNum % 2) + strBinary
            eachNum = eachNum // 2
        map1.append(strBinary)
    
    #map2       
    for eachNum2 in arr2:
        strBinary = ""
        for _ in range(n):
            strBinary = str(eachNum2 % 2) + strBinary
            eachNum2 = eachNum2 // 2
        map2.append(strBinary)
    
    #whole map
    answer = [ "".join(' ' if int(map1[i][j]) + int(map2[i][j]) == 0 else '#' for j in range(n) ) for i in range(n) ]
    
    return answer

#개선된 코드
def solution2(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        
        eachBinary = bin(arr1[i]|arr2[i])[2:].zfill(n)
        
        converted = "".join("#" if each == '1' else " " for each in eachBinary )
        answer.append(converted)
    
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = 	[30, 1, 21, 17, 28]
# n = 6
# arr1 = [46, 33, 33 ,22, 31, 50]
# arr2 = [27 ,56, 19, 14, 14, 10]
answer = solution2(n, arr1, arr2)
print(answer)