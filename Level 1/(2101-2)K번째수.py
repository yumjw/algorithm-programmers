def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        sorted_array = array[i - 1:j]
        sorted_array.sort()
        temp_answer = sorted_array[k-1]

        answer.append(temp_answer)

    return answer

# Recommended Answer
def solution_recommended(array, commands):
    return list(
        map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands)
    )