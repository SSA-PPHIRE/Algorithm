# 정렬하고, 가장 앞, 뒤 더한 것이 limit보다 큰지 판단하자
# 1차시 - 75점 (효율성 부분 실패)

def solution(people, limit):
    answer = 0
    arr = sorted(people, reverse=True)
    while len(arr) > 1:
        if arr[0] + arr[-1] > limit:
            arr = arr[1:]
            answer += 1
        else:
            arr = arr[1:-1]
            answer += 1
    if len(arr) != 0:
        answer += 1

    return answer
