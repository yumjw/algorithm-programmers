## Wrong - Time Out
def solution_W(participant, completion):

    for i in completion:
        participant.remove(i)

    return participant[0]


## Answer
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]

