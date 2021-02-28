from itertools import combinations
from operator import itemgetter

## Answer- Overtime
def solution_all(number, k):

    number_list = list(number)
    index_list = list(range(0, len(str(number))))

    index_perms = combinations(index_list, len(index_list)-k)

    answer_candidate = [itemgetter(*i)(number_list) for i in index_perms]

    answer = ''.join(max(answer_candidate))
    return answer



## Answer-Greedy
def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop(-1)
        stack.append(num)

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)