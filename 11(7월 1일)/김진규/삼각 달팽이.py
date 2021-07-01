def solution(n):
    nn = n*(n+1)//2
    arr = [0]*nn
    now_type = 1
    now = 1
    i = 0
    j = 0
    while now <= nn:
        # type 1일 때 왼쪽 위에서 순서대로 내려가는 로직
        if now_type == 1:

            i += j
            if i >= nn or arr[i] != 0:
                now_type = 2
                i -= j
                continue

            arr[i] = now
            j += 1
            now += 1
            
        # type 2일때 제일 아래에서 오른쪽으로 한칸씩 이동하는 로직
        elif now_type == 2:

            i += 1

            if i >= nn or arr[i] != 0:
                now_type = 3
                i -= 1
                continue

            arr[i] = now
            now += 1
        
        # type 3일때 오른쪽 아래에서 순서대로 올라가는 
        elif now_type == 3:

            i -= j

            if i <= 0 or arr[i] != 0:
                now_type = 1
                i += j
                continue

            arr[i] = now
            now += 1
            j -= 1

    return arr
