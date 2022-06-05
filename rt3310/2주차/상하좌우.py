from shutil import move


def solution():
    N = int(input())
    move_list = list(input().split(' '))
    pos = [1, 1]

    for i in move_list:
        if i == 'L':
            if pos[1] == 1:
                continue
            pos[1] -= 1
        elif i == 'R':
            if pos[1] == N:
                continue
            pos[1] += 1
        elif i == 'U':
            if pos[0] == 1:
                continue
            pos[0] -= 1
        else:
            if pos[0] == N:
                continue
            pos[0] += 1
    
    return ' '.join(list(map(str, pos)))

print(solution())