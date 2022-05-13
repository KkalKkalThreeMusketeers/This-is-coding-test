def solution():
    answer = 0
    row, col = list(map(int, input().split()))
    arr = []
    for i in range(row):
        tmp = list(map(int, input().split()))
        arr.append(tmp)
        
    min_arr = []
    for i in arr:
        min_arr.append(min(i))    
    answer = max(min_arr)
    
    return answer

print(solution())