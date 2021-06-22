def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        min_val = heapq.heappop(scoville)
        if min_val >= K:
            return answer
        else:
            mix_val = min_val + 2 * heapq.heappop(scoville)
            heapq.heappush(scoville, mix_val)
            answer += 1

    if scoville[0] > K:
        return answer
    else:
        return -1
