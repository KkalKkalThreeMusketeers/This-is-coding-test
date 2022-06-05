
N, M = list(map(int, input().split()))
py, px, d = list(map(int, input().split()))
pos = [py, px]
move_count = 0

# 0: 북
# 1: 동
# 2: 남
# 3: 서

move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
map_array = []
for i in range(N):
    row = list(map(int, input().split()))
    map_array.append(row)

turn_count = 0
map_array[pos[0]][pos[1]] = 1
move_count += 1
while True:
    d = (d - 1) % 4
    turn_count += 1
    
    if turn_count == 5:
        vertical = pos[0] + move[(d-2) % 4][0]
        horizontal = pos[1] + move[(d-2) % 4][1]
        if vertical < 0 or vertical >= N or horizontal < 0 or horizontal >= M:
            break
        if map_array[vertical][horizontal] == 1:
            break
        pos[0] = vertical
        pos[1] = horizontal
        turn_count = 0
        continue
    
    vertical = pos[0] + move[d][0]
    horizontal = pos[1] + move[d][1]
    
    print(vertical, horizontal)
    if vertical < 0 or vertical >= N or horizontal < 0 or horizontal >= M:
        continue
    if map_array[vertical][horizontal] == 1:
        continue
    
    pos[0] = vertical
    pos[1] = horizontal
    map_array[pos[0]][pos[1]] = 1
    turn_count = 0
    move_count += 1

print(move_count)
    