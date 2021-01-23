# Answer
def solution(answers):
    number_of_problems = len(answers)

    p1 = [1,2,3,4,5] * (number_of_problems//5) + [1,2,3,4,5][:number_of_problems%5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * (number_of_problems//8) + [2, 1, 2, 3, 2, 4, 2, 5][:number_of_problems%8]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (number_of_problems//10) + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][:number_of_problems%10]

    answer_count = [0, 0, 0]

    for i in range(number_of_problems):
        if answers[i] == p1[i]:
            answer_count[0] += 1
        if answers[i] == p2[i]:
            answer_count[1] += 1
        if answers[i] == p3[i]:
            answer_count[2] += 1

    answer = []
    max_correct = max(answer_count)

    for idx, count in enumerate(answer_count):
        if count == max_correct:
            answer.append(idx+1)

    return answer


# Recommended Answer - 공간복잡도 고려
from itertools import cycle

def solution_R(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]