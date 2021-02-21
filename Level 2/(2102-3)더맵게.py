# Answer - Overtime
def solution(scoville, K):

    scoville.sort(reverse=True)
    answer = 0

    while scoville[-1] < K:
        scoville.append(scoville.pop(-1) + scoville.pop(-1)*2)
        scoville.sort(reverse=True)
        answer +=1

        if len(scoville) < 2:
            break

    if scoville[-1] >= K:
        return answer
    else:
        return -1


# Answer by heapq
import heapq

def solution_heapq(scoville, K):
    heap = []

    for food in scoville:
        heapq.heappush(heap, food)
    answer = 0
    while heap[0] < K:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer +=1

        if len(heap) < 2:
            break

    if heap[-1] >= K:
        return answer
    else:
        return -1


print(solution_heapq([1, 2, 3, 9, 10, 12], K=7))