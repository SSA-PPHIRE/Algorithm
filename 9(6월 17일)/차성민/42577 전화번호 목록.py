def solution(phone_book):
    answer = True

    # 짧은 문자열부터 나오도록 정렬 (짧은게 접두어로 쓰일 확률이 높으므로)
    phone_book.sort()

    # 한 전화번호가 다른 번호의 접두사면 answer를 false로 바꿔주고 break
    for i in range(len(phone_book) - 1):
        # 첫 문자열이 접두사로 있는지 확인하기 위해 phone_book[i]의 길이만큼만 가져와서 비교
        if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            answer = False
            break

    return answer

### 효율성 통과는 했는데 높지는 않음

## 해시로 분류가 되어있어서 해시로 풀어야하나했는데 해시 코드 찾아서 돌렸는데 동일하게 나와서 당황

## 해쉬 풀이
'''
def solution(phone_book):
    answer = True

    hash = {}

    for num in phone_book:
        hash[num] = 1

    for num in phone_book:
        tmp = ""
        for number in num:
            tmp += number
            if tmp in hash and tmp != num:
                return False

    return answer
'''
