N = input()

pos = [int(N[1]), int(ord(N[0])) - int(ord('a')) + 1]

possible_straight_count = 4

if pos[0] <= 2 or pos[0] >= 7:
    possible_straight_count -= 1
if pos[1] <= 2 or pos[1] >= 7:
    possible_straight_count -= 1
    
possible_turn_count = possible_straight_count * 2

if pos[0] <= 1 or pos[0] >= 8:
    if pos[1] <= 2 or pos[1] >= 7:
        possible_turn_count -= 1
    else:
        possible_turn_count -= 2
if pos[1] <= 1 or pos[1] >= 8:
    if pos[0] <= 2 or pos[0] >= 7:
        possible_turn_count -= 1
    else:
        possible_turn_count -= 2

print(possible_turn_count)