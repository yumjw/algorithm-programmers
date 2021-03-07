def solution(n):
    answer = 0
    ternary_list = []

    while n >= 3:
        ternary_list.append(str(n % 3))
        n = n // 3

    ternary_list.append(str(n % 3))
    ternary = int(''.join(ternary_list))

    digit = 0
    while ternary >= 10:
        answer += (ternary % 10) * 3 ** digit
        ternary = ternary // 10
        digit += 1

    answer += (ternary % 10) * 3 ** digit

    return answer

print(solution(125))