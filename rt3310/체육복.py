def solution(n, lost, reserve):
    answer = 0

    students = [1 for i in range(n)]
    for i in lost:
        students[i - 1] -= 1

    for i in reserve:
        students[i - 1] += 1

    for i, v in enumerate(students):
        if v == 0:
            if (i > 0) and students[i - 1] == 2:
                students[i - 1] -= 1
                students[i] += 1
                continue
            if (i < len(students) - 1) and students[i + 1] == 2:
                students[i + 1] -= 1
                students[i] += 1
                continue

    answer = len(list(filter(lambda x: x > 0, students)))
    return answer

solution(5, [2, 4], [1, 3, 4])
solution(5, [2, 4], [3])
