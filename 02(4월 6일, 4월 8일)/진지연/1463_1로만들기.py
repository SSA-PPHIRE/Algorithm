# 6으로 나눴을 때의 나머지로 정한다

def get_operation(n):
    remainder = n%6
    if remainder == 1 or remainder == 5 or remainder == 4:
        return n-1
    elif remainder == 2:
        return n/2
    else: # remainder == 3 or 6
        return n/3

n = int(input())
cnt = 0
while n != 1:
    n = get_operation(n)
    cnt += 1

print(cnt)




# index error

n = int(input())
arr = [0 for _ in range(n+1)]
arr[1] = 0
arr[2] = 1
arr[3] = 1

def get_operation(n):
    remainder = n % 6
    if remainder == 1:
        arr[n] = arr[n-1] + 1
    elif remainder == 2:
        arr[n] = min(arr[n-1], arr[n//2]) + 1
    elif remainder == 3:
        arr[n] = min(arr[n-1], arr[n//3])+1
    elif remainder == 4:
        arr[n] = min(arr[n//2], arr[n-1]) + 1
    elif remainder == 5:
        arr[n] = arr[n-1] + 1
    else:
        arr[n] = min(arr[n//2], arr[n//3], arr[n-1]) +1

for i in range(4, n+1):
    get_operation(i)

print(arr[n])

