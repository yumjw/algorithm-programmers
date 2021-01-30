import itertools

def solution(new_id):
    new_id = new_id.lower()
    for i in list(set(new_id) - set('abcdefghijklmnopqrstuvwxyz1234567890-_.') ):
        new_id = new_id.replace(i,'')

    temp = ''
    for k, v in itertools.groupby(new_id):
        value = list(v)
        if set(value) != set('.'):
            temp += ''.join(value)
        else:
            temp += '.'
    new_id = temp

    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if new_id == '':
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]

    return new_id


# Recommended Answer - Regular Expression
import re

def solution_R(new_id):
    answer = new_id
    answer = answer.lower() #1
    answer = re.sub('[^a-z0-9\-_.]', '', answer) #2
    answer = re.sub('\.+', '.', answer) #3
    answer = re.sub('^[.]|[.]$', '', answer) #4
    answer = 'a' if len(answer) == 0 else answer[:15] #5
    answer = re.sub('^[.]|[.]$', '', answer)
    answer = answer if len(answer) > 2 else answer + "".join([answer[-1] for i in range(3-len(answer))])
    return answer