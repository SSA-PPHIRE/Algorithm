def solution(numbers, target):

    def check(idx, sum_val, cnt):

        if idx == len(numbers):
            if target == sum_val:
                cnt += 1
            return cnt

        cnt = check(idx + 1, sum_val + numbers[idx], cnt)
        cnt = check(idx + 1, sum_val - numbers[idx], cnt)
        return cnt

    answer = check(0, 0, 0)

    return answer
