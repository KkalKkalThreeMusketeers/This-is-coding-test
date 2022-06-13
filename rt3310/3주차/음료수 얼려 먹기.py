row, column = list(map(int, input().split()))

graph = []
for i in range(row):
    tmp = list(map(int, input()))
    graph.append(tmp)
    
def dfs(x, y):
    if x < 0 or x >= column or y < 0 or y >= row:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(column):
    for j in range(row):
        if dfs(i, j) == True:
            result += 1
            
print(result)
        