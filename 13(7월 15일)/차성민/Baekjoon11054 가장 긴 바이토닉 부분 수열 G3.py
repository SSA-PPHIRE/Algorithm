#백준 11054 가장 긴 바이토닉 부분 수열 G3

'''
조건: 각 1000이하

1. 가장 큰 수 기준으로 좌측, 우측 체크 (가장 큰 수는 중복 되니까 결과에서 -1 해줘야 함.)
2. 조건에 맞게 범위 지정해주고 탐색하면 될듯

* 좌측부터 증가되는거 체크하고 우측부터 감소되는거 체크했더니 딱히 큰수의 위치 등은 관계가 없었음
* 그냥 좌측 체크 +  우측 체크 -1하면 끝

크기를 각각 1000으로 지정해줬더니 다른 사람들 코드보다 시간은 많이 나옴

'''

n = int(input())
a = list(map(int, input().split()))
res = 0

dp_left = [1] * 1000
dp_right = [1] * 1000

for i in range(n): # 좌측부터 체크
    for j in range(i):
        if a[i] > a[j]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)

for i in range(n-1, -1, -1):  # 우측부터 체크
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)

for i in range(n): #res에 값 넣어줌
    if dp_left[i]+dp_right[i] > res:
        res = dp_left[i] + dp_right[i]

print(res - 1) # 가장 큰 수가 겹치니까 빼줌
