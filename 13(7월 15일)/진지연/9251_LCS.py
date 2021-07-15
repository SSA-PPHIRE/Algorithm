'''
구현에 초점을 두었다..
'''

col = '0'+input()
row = '0'+input()

arr = [[0]*len(col) for _ in range(len(row))]

for r in range(len(row)):
    for c in range(len(col)):
        if r == 0 or c == 0:
            continue
        # print(r,row[r], c,col[c])
        if row[r] == col[c]:
            arr[r][c] = arr[r-1][c-1]+1
        else:
            arr[r][c] = max(arr[r][c-1], arr[r-1][c])
print(arr[len(row)-1][len(col)-1])
