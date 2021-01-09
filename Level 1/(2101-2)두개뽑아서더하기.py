def solution(numbers):
    numbers_index = list(range(len(numbers)))
    answer = []
    for idx1 in range(len(numbers_index) - 1):
        for idx2 in range(idx1 + 1, len(numbers_index)):
            answer.append(numbers[idx1] + numbers[idx2])

    answer = list(set(tuple(answer)))
    answer.sort()
    return answer