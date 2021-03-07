def solution(priorities, location):
    answer = 0


    temp = priorities.pop(0)

    while

    while location > 0:
        if temp < max(priorities):
            priorities.append(temp)
            location -= 1
        else:
            answer += 1
            location -=1



    return answer