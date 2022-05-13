def solution(number, k):
    answer = ''

    numbers = []
    for i in number:
        numbers.append(i)

    numbers = list(map(int, numbers))

    remove_list = []
    count = k
    for i in range(0, len(numbers)):
        if number[i] == 9:
            continue
        if len(numbers) - i == count:
            remove_list.extend(numbers[i:])
            break
        for j in range(1, count + 1):
            if numbers[i] < numbers[i+j]:
                remove_list.append(numbers[i])
                count -= 1
                break
        if len(remove_list) == k:
            break
    
    for i in remove_list:
        numbers.remove(i)
    answer = ''.join(map(str, numbers))
    return answer


solution("4177252841", 4)
