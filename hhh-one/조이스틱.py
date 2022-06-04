def solution(name):
    answer = 0
    answer = len(name) - 1 #한 방향일 때
    
    #좌우
    i = 1
    while i < len(name):
        if name[i] == "A":
            R = i - 1
            i += 1
            while i < len(name) and name[i] == "A":
                i += 1
            L = len(name) - i
            answer = min([answer, 2 * R + L, 2 * L + R])
        else:
            i += 1
            
    #상하
    for i in name:
        U = abs(ord(i) - ord("A"))
        D = abs(ord("Z") - ord(i))
        answer += min([U, D + 1])

    return answer