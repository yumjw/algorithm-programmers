import math

def solution(s):
    if len(s)%2 == 1:
        return s[math.ceil(len(s)/2)-1]
    else:
        return s[math.ceil(len(s)/2)-1:math.ceil(len(s)/2)+1]


## Recommended Answer
# 굳이 if문과 나머지를 이용할 필요 없이 바로 몫으로 계산해도 됨.

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
