# 효율성 시간 초과로 실패

def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].find(phone_book[i]) == 0:
                answer = False
                return answer
    return answer
