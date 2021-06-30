# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    
    num_of_1 = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == num_of_1:
            answer = n
            break
        
    return answer
