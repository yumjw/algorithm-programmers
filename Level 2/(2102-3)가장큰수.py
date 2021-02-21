# Answer - Permutations
from itertools import permutations


def solution(numbers):
    numbers = list(map(str,numbers))

    perms = list(permutations(numbers, len(numbers)))
    answer_candidate = [''.join(map(str, i)) for i in perms]
    answer = max(answer_candidate)

    return ''.join(answer)


# Recommend Answer - list sort method by lambda
def solution_lambda(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))
