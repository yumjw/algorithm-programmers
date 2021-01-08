import numpy as np

def solution(board, moves):
    board = np.array(board)
    depth = []
    size = board.shape[0]

    for column in range(size):
        for row in range(size):
            if board[row, column] != 0:
                depth.append(row)
                break

    answer = 0
    ListisEmpty = True
    bucket = []

    for move in moves:
        if len(bucket) == 0:
            ListisEmpty = True

        move = move - 1

        if depth[move] >= size:
            continue

        picked_doll = board[depth[move], move]


        if ListisEmpty is True:
            bucket.append(picked_doll)
            board[depth[move], move] = 0
            ListisEmpty = False

        else:
            if bucket[-1] == picked_doll:
                bucket.pop(-1)
                answer += 2
            else:
                bucket.append(board[depth[move], move])
            board[depth[move], move] = 0

        depth[move] = depth[move] + 1

    return answer



# Recommended Answer
def solution_recommended(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer