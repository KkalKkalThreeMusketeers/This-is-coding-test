def solution(n, lost, reserve):
    answer = 0

    answer += n - len(lost)  #체육복을 가지고 있는 학생들
    
    #잃어버렸지만 여분의 체육복이 있는 학생들
    for l in lost:
        for r in reserve:
            if(l == r):
                reserve.remove(r)
                lost.remove(l)
                answer += 1

    for l in lost:
        for r in reserve:
            if(l == r - 1 or l == r + 1): #lost 기준 앞 뒤일 때
                answer += 1
                reserve.remove(r)
                break #앞 뒤 중복해서 빌리는 경우를 제외하기 위함
    return answer