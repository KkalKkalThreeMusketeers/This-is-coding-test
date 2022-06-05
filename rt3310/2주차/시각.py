# 3 13 23 30 31 32 33 34 35 36 37 38 39 43 53
def solution():
    N = int(input())
    one_case_count = 15 * 45 * 2 + 15 * 15
    hour_three_case_count = N // 3

    return ((N + 1) * one_case_count) + (hour_three_case_count * 60 * 60) - (hour_three_case_count * one_case_count)

print(solution())