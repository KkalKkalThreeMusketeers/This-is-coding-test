from collections import deque
from shutil import move

n, m = list(map(int, input().split()))

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
 
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([nx, ny])
                
    return graph[n-1][m-1]
            
print(bfs(0,0))