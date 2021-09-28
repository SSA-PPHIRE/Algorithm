'''
어떤 기준으로 어떤 값을 이분탐색할 것인가?

주어진 시간동안 각 심사관이 n명을 모두 검사할 수 있는가?
그 중에서 최소값은 얼마인가?
'''

def solution(n, times):
    answer = 0
    low = 0
    high = max(times) * n

    while low <= high:

        # 입국심사 최소 시간
        mid = (low + high) //2

        count = 0
        for time in times:
            count = count + mid // time

            # 모든 인원을 검사 가능 하면 break
            if count >= n:
                break

        # 모든 인원을 검사 가능하면 answer을 업데이트 해주고
        # 최소 시간을 줄여나간다.
        if count >= n :
            high = mid - 1
            answer= mid
        # 모든인원을 검사 할수 없으면 최소 시간을 늘린다.
        else :
            low = mid +1


    return answer
