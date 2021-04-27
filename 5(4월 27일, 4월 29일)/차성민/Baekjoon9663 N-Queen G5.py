## 풀이법 1

### 케이스가 15개니까 그냥 다 구해주고 출력시킴

'''
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])
'''

## 풀이법 2

### DFS(재귀), 백트래킹 적용해주면 끝
### 가로체크, 대각선 체크, 반대편 대각선 체크


def chk(index): # 열, 대각선 체크
    for i in range(index):
        if row[index] == row[i]: # 같은 열에 있으면 X
            return 0
        elif abs(row[index] - row[i]) == index - i: # 대각선에 있으면 X
            return 0
    return 1


def DFS(idx):
    global answer

    if idx == n:
        answer += 1

    else:
        # 행에 놓으며 진행
        for i in range(n): # 열번호를 0부터 증가시키며 가능한 곳을 찾아줌.
            row[idx] = i
            if chk(idx): #chk를 통해 행,열, 대각선에 걸리는게 없으면 계속 진행하고 아니면 멈춤( 백트래킹)
                DFS(idx + 1)


n = int(input())
row = [0] * n # 이중리스트가 아닌 단일 리스트로 설정 # row의 idx는 행의 값, row[idx]는 열의 값
answer = 0
DFS(0)
print(answer)
