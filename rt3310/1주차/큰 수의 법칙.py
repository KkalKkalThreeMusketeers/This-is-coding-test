def solution():
    n, m, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    answer = 0

    sorted_arr = sorted(arr, reverse=True)
    for i, v in enumerate(sorted_arr):
        print(v)

    count = 0
    seq_count = 0
    while count < m:
        if seq_count < k:
            answer += sorted_arr[0]
            seq_count += 1
        else:
            answer += sorted_arr[1]
            seq_count = 0
        count += 1
        
    return answer

print(solution())