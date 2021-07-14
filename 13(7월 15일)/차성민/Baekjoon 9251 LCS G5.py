#백준 9251 LCS G5
'''
행렬 만들고 보면 규칙 보임

'''

str1 = list(str(input()))
str2 = list(str(input()))

arr = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
res = 0


for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]: # 같은 값이면 + 1
            arr[j][i] = arr[j-1][i-1] + 1
            res = max(res, arr[j][i])
        else: # 아니면 대각선 값들 중 큰 값
            arr[j][i] = max(arr[j][i-1], arr[j-1][i])

print(res)
