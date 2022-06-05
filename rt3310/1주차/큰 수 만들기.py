def solution(number, k):
    answer = ''

    numbers = []
    for i in number:
        numbers.append(i)

    numbers = list(map(int, numbers))
    
    i = 0
    cnt = 0
    while cnt < k and i < len(numbers):
        if numbers[i] == 9:
            i += 1
            continue

        for j in numbers[i+1:k-cnt+i+1]:
            if numbers[i] < j:
                numbers = numbers[:i] + numbers[i+1:]
                cnt += 1
                break
        else:
            i += 1
    
    answer = ''.join(map(str, numbers[:len(numbers) - (k - cnt)]))
    return answer


print(solution("987654321", 4))
