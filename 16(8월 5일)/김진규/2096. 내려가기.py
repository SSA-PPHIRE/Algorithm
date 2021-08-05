n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pre_max_res = [0, 0, 0]
now_max_res = [-1, -1, -1]
pre_min_res = [0, 0, 0]
now_min_res = [1000000, 1000000, 1000000]
tmp_max = [0, 0, 0]
tmp_min = [0, 0, 0]

if n == 1:
    print(max(arr[0]), end=' ')
    print(min(arr[0]))

else:

    for i in range(3):
        pre_max_res[i] = arr[0][i]
        pre_min_res[i] = arr[0][i]

    for i in range(1, n):
        for j in range(3):
            if j == 0:
                if pre_max_res[j] + arr[i][j] > now_max_res[j]:
                    now_max_res[j] = pre_max_res[j] + arr[i][j]
                if pre_max_res[j + 1] + arr[i][j] > now_max_res[j]:
                    now_max_res[j] = pre_max_res[j + 1] + arr[i][j]

                now_min_res[j] = pre_min_res[j] + arr[i][j]
                if pre_min_res[j + 1] + arr[i][j] < now_min_res[j]:
                    now_min_res[j] = pre_min_res[j + 1] + arr[i][j]
            elif j == 1:
                if pre_max_res[j-1] + arr[i][j] > now_max_res[j]:
                    now_max_res[j] = pre_max_res[j-1] + arr[i][j]
                if pre_max_res[j] + arr[i][j] > now_max_res[j]:
                    now_max_res[j] = pre_max_res[j] + arr[i][j]
                if pre_max_res[j + 1] + arr[i][j] > now_max_res[j]:
                    now_max_res[j] = pre_max_res[j + 1] + arr[i][j]

                now_min_res[j] = pre_min_res[j - 1] + arr[i][j]
                if pre_min_res[j] + arr[i][j] < now_min_res[j]:
                    now_min_res[j] = pre_min_res[j] + arr[i][j]
                if pre_min_res[j + 1] + arr[i][j] < now_min_res[j]:
                    now_min_res[j] = pre_min_res[j + 1] + arr[i][j]
            else:
                if pre_max_res[j - 1] + arr[i][j] > now_max_res[j]:
                    now_max_res[j] = pre_max_res[j - 1] + arr[i][j]
                if pre_max_res[j] + arr[i][j] > now_max_res[j]:
                    now_max_res[j] = pre_max_res[j] + arr[i][j]

                now_min_res[j] = pre_min_res[j - 1] + arr[i][j]
                if pre_min_res[j] + arr[i][j] < now_min_res[j]:
                    now_min_res[j] = pre_min_res[j] + arr[i][j]

        pre_min_res = now_min_res[:]
        pre_max_res = now_max_res[:]

    print(max(now_max_res), end=' ')
    print(min(now_min_res))
