### 백준 1644 소수의 연속합 G3

#### 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수 출력



0) 코드

```python
import sys
sys.stdin = open('text/1644.txt', 'r')

n = int(input())
arr = [0] * (n + 1) # 빈 리스트 만들고 에라토스 테네스 체 활용
prime = []
res = 0 #경우의 수 출력용

# 에라토스 테네스 체로 소수면 1 아니면 다른 값으로 넣어줌
for i in range(2, n+1):
    if arr[i] == 0:
        arr[i] = 1
        prime.append(i)
        for j in range(i+i, n+1, i):
            arr[j] = 3

# 투포인터 활용하여 구해주고 원하는 값 나올때마다 res 증가
l, r = 0, 0 # 포인터 설정
temp = 0  # 현재까지의 합을 위한 변수

## 내가 놓친 것 : 소수인 것들만 모아서 리스트를 만들어주고 활용하면 훨씬 쉬웠을 텐데

while True:
    if temp >= n: #현재까지의 합이 n보다 크면 가장 좌측 값빼고 좌측포인터 증가시키고 진행
        temp -= prime[l]
        l += 1
    elif r == len(prime): # 끝까지 오면 break
        break
    else: # 합이 n보다 작으면 우측값 추가 후 우측 포인터 증가시키고 진행
        temp += prime[r]
        r += 1

    if temp == n: #현재까지의 합이 n이면 res 증가시킴.
        res += 1
print(res)
```



1) 첫 구현 로직
![1644 logic](https://user-images.githubusercontent.com/51193582/116994818-311f0600-ad14-11eb-8619-4690852c1c4c.jpg)



2) 코드 작성 및 문제점 발견

```python
# while l < n+1:  #좌측 인덱스값을 기준으로 탐색
#     if temp == n: # 값이 n이면 res를 증가시킨 후에 좌측 포인터를 1증가시켜 다음번부터 진행
#         res += 1
#         temp = 0
#         l += 1
#         r = l+1
#         continue
#
#
#     if r == n+1 and temp < n: #우측 포인터가 끝 값일 때
#         # if temp < n: # 1. 값이 이래도 n보다 작으면 break
#             break
#
#     if temp < n: #값이 n보다 작으면 우측 칸 체크 후, 소수면 더해줌
#         if arr[r] == 1:
#             temp += r
#             r += 1
#         else:
#             r += 1
#
#     if temp > n: #값이 n보다 크면 가장 좌측 값 체크 후, 가장 적은 값을 빼면서 조정
#
#         if arr[l] == 1:
#             temp -= l
#             l += 1
#         else:
#             l += 1
```

while 문을 다음과 같이 작성하며 느낀 것은 너무 탐색에 오랜 시간이 걸리기도 하고, 중간에 temp> n인 상태로 쭉 이어지다가 끝나버리는 경우가 몇 번 있어서 이거 처리가 문제였음.



3) 문제 해결

에라토스 테네스 체로 만들 때, 소수인 값들로 이루어진 Prime 리스트를 같이 만들어주고

이 리스트 안에서만 투포인터를 활용한 탐색을 진행하면 간단해질거다



이를 적용시키고 해결.

