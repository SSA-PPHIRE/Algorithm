# 처음에 그냥 3, 2, 1 순서대로 진행 -> 실패
# 설명에 다이나믹 프로그래밍이라 되어 있는 것을 봄
# DP 사용 결정
# 100만개의 배열을 만들고 일일히 조회한다면 시간초과가 걸릴 것이라 생각
# but 생각보다 널널

N = int(input())
# 최댓값이 100만이므로 index를 100만+1로 설정
# diff1 = lst[i+1] + 1 에서 index error가 떠서 +1 더 해줌
lst = [0]*1000002
# 입력한 값으로 부터 1씩 감소하며
# 현재 index 값을 가지기 위한 최소 횟수를 구함
for i in range(N, 0, -1):
    # 만약 현재 index * 2를 한 값이 범위 내라면 그 값 + 1을 한 값이
    # 2로 나누었을 때의 최소 횟수
    if i * 2 <= N:
        multi2 = lst[i*2] + 1
    # 그렇지 않다면 9999를 대입해 가장 큰 값으로 만듦
    # -> min 연산에 영향을 미치지 않기 위해
    else:
        multi2 = 9999
    # 만약 현재 index * 3을 한 값이 범위 내라면 그 값 + 1을 한 값이
    # 3으로 나누었을 때의 최소 횟수
    if i * 3 <= N:
        multi3 = lst[i*3] + 1
    # 그렇지 않다면 9999를 대입해 가장 큰 값으로 만듦
    # -> min 연산에 영향을 미치지 않기 위해
    else:
        multi3 = 9999
    # 이전 index에서 1을 감소 시켰을 때의 값
    diff1 = lst[i+1] + 1
    # 위의 연산에서 나온 값들 중 최솟값을 현재의 index에 저장
    lst[i] = min(multi2, multi3, diff1)
# index 1일 때의 값을 출력
# -1을 해주는 이유는 index가 N일때 1이 더해져 있기 때문
print(lst[1]-1)
