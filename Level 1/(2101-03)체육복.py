## Greedy

#Answer
def solution(n, lost, reserve):
    check_list = [1] * n
    reserve_list = [0] * n

    for i in lost:
        check_list[i-1] = 0

    for i in reserve:
        if check_list[i-1] == 0:
            check_list[i-1] = 1
            continue
        else:
            reserve_list[i-1] = 1

    for idx, check in enumerate(check_list):
        if idx == 0:
            if check == 0:
                if reserve_list[idx+1] == 1:
                    check_list[idx] += 1
                    reserve_list[idx+1] -= 1

        elif idx == n-1:
            if check == 0:
                if reserve_list[idx-1] ==1:
                    check_list[idx] += 1
                    reserve_list[idx-1] -= 1
        else:
            if check == 0:
                if (reserve_list[idx-1] + reserve_list[idx +1]) >= 1:
                    if reserve_list[idx-1] == 1 and reserve_list[idx +1] >=0:
                        check_list[idx] += 1
                        reserve_list[idx-1] -= 1
                    else:
                        check_list[idx] += 1
                        reserve_list[idx + 1] -= 1
    answer = sum(check_list)

    return answer


# Recommended Answer
def solution_R(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)