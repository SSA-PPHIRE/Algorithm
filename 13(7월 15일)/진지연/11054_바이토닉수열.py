'''
부분수열을 구해야 함.. 이건 x
'''

n = int(input())
arr = list(map(int, input().split()))

def inspect(pointer):
    global n
    flag = 0    # 0은 증가, 1은 감소라 하자
    start = pointer
    while True:
        # print(pointer)
        if pointer == n-1:
            break
        if flag == 0:
            if arr[pointer] < arr[pointer+1]:
                pointer += 1
            elif arr[pointer] > arr[pointer+1]:
                pointer += 1
                flag += 1
            else:
                break
        elif flag == 1:
            if arr[pointer] > arr[pointer + 1]:
                pointer += 1
            else:
                break
    # print('*********************')
    return pointer, pointer - start + 1


ans = 0
pointer = 0
tmp = 0
while True:
    if tmp > ans:
        ans = tmp
    if pointer == n-1:
        break

    pointer, tmp = inspect(pointer)
    # print(pointer, tmp)
print(ans)




