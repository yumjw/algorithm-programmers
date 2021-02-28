# Answer by Product - 시간초과
from itertools import product

def square(number):
    return int((3 ** (number + 1) - 1) / 2) - 1

def solution(n):
    digit = 0
    answer_candidate = []

    while n > square(digit):
        digit +=1
        sub = square(digit) - n

    for i in list(product(['1','2','4'], repeat=digit)):
        answer_candidate.append(int(''.join(i)))

    answer_candidate.sort(reverse=False)

    return str(answer_candidate[-(sub+1)])


# Recommended Answer - Sibal...
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer
