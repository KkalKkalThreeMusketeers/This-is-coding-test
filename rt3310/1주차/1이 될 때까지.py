def solution():
    n, k = list(map(int, input().split()))
    answer = 0

    while n != 1:
        if n % k == 0:
            n //= k
            count += 1
        else:
            n -= 1
            count += 1
            
    return answer

print(solution())