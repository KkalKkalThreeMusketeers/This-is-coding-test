def solution(sizes):
    answer = 0
    w_list = []
    h_list = []
    for w, h in sizes:
        if w < h:
            w, h = h, w
        w_list.append(w)
        h_list.append(h)
    answer = max(w_list) * max(h_list)
    return answer