import string

## ANSWER
def count_up_down(target):
    return min(string.ascii_uppercase.index(target), 26-string.ascii_uppercase.index(target))


def solution(name):
    answer = 0
    current_index = 0
    check_done = [1] * len(name)

    for idx, value in enumerate(name):
        if value == 'A':
            check_done[idx] -= 1

    not_done_index = [idx for idx, element in enumerate(check_done) if element > 0]
    print(not_done_index)
    if count_up_down(name[-1]) > count_up_down((name[1])):
        direction = -1
    else:
        direction = 1

    while len(not_done_index) > 0:
        answer += count_up_down(name[current_index])
        print(current_index)

        if (current_index + 7)%len(name) in not_done_index:
            not_done_index.remove((current_index + 7)%len(name))


        current_index += direction
        answer += 1

    return answer