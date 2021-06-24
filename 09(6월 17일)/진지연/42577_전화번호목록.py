# https://programmers.co.kr/learn/courses/30/lessons/42577

# 문자열을 정렬하면 어떻게 되는지 주목
# 효율성 통과 못함
import re
def solution(ipt):
    ipt.sort()
    for i in range(len(ipt)-1):
        if re.match(ipt[i], ipt[i+1]):
            return False
    return True

# 다르 사람 풀이
def solution(phone_book):
    phone_book.sort()
    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
