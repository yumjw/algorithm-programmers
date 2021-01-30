import itertools

def solution(arr):

    grouped = itertools.groupby(arr)
    answer = [k for k, v in grouped]

    return answer


## Recommended Answer
def solution_R(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result