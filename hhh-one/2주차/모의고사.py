import math
def solution(answers):
    answer = []
    a1 = a2 = a3 = 0
    l1 = [1, 2, 3, 4, 5] * math.ceil(len(answers) / 5)
    l2 = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(len(answers) / 8)
    l3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(len(answers) / 10)
    for i in range(len(answers)):
        if answers[i] == l1[i]:
            a1 += 1
        if answers[i] == l2[i]:
            a2 += 1
        if answers[i] == l3[i]:
            a3 += 1
            
    if max(a1, a2, a3) == a1:
        answer.append(1)
    if max(a1, a2, a3) == a2:
        answer.append(2)
    if max(a1, a2, a3) == a3:
        answer.append(3)
    return answer