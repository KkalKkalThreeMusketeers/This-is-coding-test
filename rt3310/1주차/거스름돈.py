def solution(money):
    answer = 0
    
    answer += (money // 500)
    money %= 500
    
    answer += (money // 100)
    money %= 100
    
    answer += (money // 50)
    money %= 50
    
    answer += (money // 10)
    
    return answer

print(solution(1260))

