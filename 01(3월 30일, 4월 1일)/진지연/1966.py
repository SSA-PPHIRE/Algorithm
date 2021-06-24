T = int(input())

for tc in range(T):

    # 인풋받기
    n, idx = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    # 열이 두개 필요함. 중요도 열과, 초기 위치열 
    idxs = [i for i in range(n)]

    # for로 잡으면 몇번 돌지 정해야 해서 while로 함
    while True:
        # 종료조건
        if not arr:
            break
        
        ### queue의 첫번째 값을 mx로 두고
        mx = arr[0]
        mx_idx = idxs[0]
        ### 대기열에 더 큰값이 있는지 확인함
        for i in range(len(arr)):
            if mx < arr[i]:
                mx = arr[i]

                arr.append(arr.pop(0))
                idxs.append(idxs.pop(0))
                ### 더 큰값이 하나라도 있으면 넘김. 
                # break 없으면 시간초과 뜸!
                break
        ### 대기열에 더 큰값이 없으면
        if idxs[0] == mx_idx:
            arr.pop(0)
            idxs.pop(0)
            if mx_idx == idx:
                rnk = n - len(idxs) + 1
                print(rnk)
                break
