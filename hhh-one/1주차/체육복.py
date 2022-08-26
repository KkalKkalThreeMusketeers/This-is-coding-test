def solution(n, lost, reserve):
    # 체육복(uniform) 수를 나타내는 학생 수, 앞 뒤로 한명씩 추가
    u = [1] * (n + 2) 
    
    for i in lost:
        u[i] -= 1
    for i in reserve:
        u[i] += 1
     
    # 체육복이 없는 학생 기준으로 앞 -> 뒤 로 빌림
    for i in range(1, n + 1):
        if u[i] == 0 and u[i - 1] == 2:
            u[i - 1:i + 1] = [1, 1]
        elif u[i] == 0 and u[i + 1] == 2:
            u[i:i + 2] = [1, 1]
            
    return len([x for x in u[1:-1] if x > 0])