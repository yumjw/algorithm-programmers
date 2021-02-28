## Stack, Queue

import math

# ?
def solution_d(progresses, speeds):
    remaining_progress = map(lambda x: 100-x, progresses)
    days_need_per_progress = list(map(lambda x, y: math.ceil(x / y), remaining_progress, speeds))

    answer = []
    delayed_deploy = 0
    index_point = 0

    for current_idx, current_day_need in enumerate(days_need_per_progress[:-1]):
        if current_idx != index_point:
            continue

        for future_idx in range(current_idx+1, len(days_need_per_progress)):
            if current_day_need >= days_need_per_progress[future_idx]:
                delayed_deploy += 1
            else:
                answer.append(delayed_deploy+1)
                delayed_deploy = 0
                index_point += (future_idx-current_idx)
    answer.append(delayed_deploy + 1)
    return answer


# Answer
def solution(progresses, speeds):
    remaining_progress = map(lambda x: 100 - x, progresses)
    days_need_for_progress = list(map(lambda x, y: math.ceil(x / y), remaining_progress, speeds))

    answer = []

    while len(days_need_for_progress) > 0:
        count = 1
        a = days_need_for_progress.pop(0)
        check = days_need_for_progress.copy()
        for i in range(len(days_need_for_progress)):
            if a >= days_need_for_progress[i]:
                count += 1
                check.pop(0)
            else:
                break
        answer.append(count)
        days_need_for_progress = check.copy()
    return answer


# Recommended Answer
def solution_R(progresses, speeds):
    queue=[]
    for p, s in zip(progresses, speeds):
        if len(queue)==0 or queue[-1][0]<-((p-100)//s):
            queue.append([-((p-100)//s),1])
        else:
            queue[-1][1]+=1
    return [q[1] for q in queue]