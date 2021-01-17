## Stack, Queue


# Answer O(N^2)
def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer


# O(N)으로 시도
def solution_N(prices):
    answer = list(range(len(prices) - 1, -1, -1))
    index_list = list(range(len(prices)))

    for current_idx, current_value in enumerate(prices[:-1]):

        queue_of_dropped = []
        _ = list(map(lambda x: queue_of_dropped.append(x) if current_value > prices[x] else 0,
                               index_list[current_idx + 1:])) #list append 적용을 위해 임의의 변수로 assign

        if len(queue_of_dropped) > 0:
            first_dropped_idx = queue_of_dropped[0]
            answer[current_idx] = (first_dropped_idx - current_idx)
    return answer


# Recommended Answer
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # stack이 비었이면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer

print(solution_N([1,2,3,2]))