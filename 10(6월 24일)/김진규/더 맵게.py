def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            return cnt
        else:
            if len(scoville) == 1:
                return -1
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            z = x+2*y
            heapq.heappush(scoville, z)
            cnt += 1
