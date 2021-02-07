def solution(n):
    square = 0
    square_list = []
    while sum(square_list) + 3**(square) <= n:
        square_list.append(3**square)
        square +=1
    return sum(square_list)

print(solution(1))