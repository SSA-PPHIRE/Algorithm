# 시간초과 : 하나만 정렬

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
schs = list(map(int, input().split()))

cards.sort()
for s in schs:
    cnt = 0
    for c in cards:
        if c == s:
            cnt += 1
        elif c > s:
            break
    print(cnt, end=' ')
    
    
    

# 시간초과 : 둘다 정렬
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
schs_unsorted = list(map(int, input().split()))


cards.sort()
schs = sorted(schs_unsorted)
ans = []

focus = 0
for s in schs:
    cnt = 0
    for i in range(focus,n):

        if cards[i] == s:
            cnt += 1
        if cards[i] > s:
            focus = i
            break
    ans.append([s, cnt])



for i in schs_unsorted:
    for j in ans:
        if i == j[0]:
            print(j[1], end=' ')
            
            

