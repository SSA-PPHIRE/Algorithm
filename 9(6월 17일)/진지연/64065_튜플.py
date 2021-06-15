# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(ipt):
    string = ipt[1:-2].split('},')                
    string.sort(key=lambda x:len(x))

    answer = []
    for s in string:
        s=list(s[1:].split(','))
        for a in answer:
            s.remove(a)
        answer.extend(s)

    # print(list(map(int, answer)))
    return list(map(int, answer))

  
# 정규표현식 사용하기
re.findall('\d+', s)
re.match(ipt[i], ipt[i+1])
p = re.compile("^"+s)
