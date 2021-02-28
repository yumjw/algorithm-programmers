def solution(strings, n):
    a = sorted(strings)
    a.sort(key=lambda x: x[n])
    return a

