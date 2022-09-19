from itertools import permutations, chain

def solution(numbers):
    answer = 0
    
    number_list = set()
    for i in range(1, len(numbers)+1):
        for j in list(map(lambda x: int(''.join(x)), list(permutations(numbers, i)))):
            number_list.add(j)
            
    for x in number_list:
        if x <= 1:
            continue
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            answer += 1
    return answer