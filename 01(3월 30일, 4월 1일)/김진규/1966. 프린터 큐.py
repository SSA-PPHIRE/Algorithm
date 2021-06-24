T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    # 기본 순서를 저장한 리스트
    order_list = [i for i in range(N)]
    # 우선 순위를 저장한 리스트
    priority_list = list(map(int, input().split()))
    # zip을 통해 둘을 합침
    purpose_list = list(zip(priority_list, order_list))
    # 출력되는 순서를 표현하기 위한 변수
    cnt = 0

    while True:
        # 우선 순위가 가장 높은 항목이 제일 앞에 있다면
        if max(purpose_list, key=lambda x: x[0]) == purpose_list[0]:
            # 가장 앞 항목을 pop
            p = purpose_list.pop(0)
            # cnt 1 증가
            cnt += 1
            # pop한 항목이 목표 대상이라면 출력 후 break
            if p[1] == M:
                print(cnt)
                break
        # 그렇지 않다면
        else:
            # 가장 앞의 항목을 제일 뒤로 이동
            p = purpose_list.pop(0)
            purpose_list.append(p)

########################################
# 두달 전 풀이(IM 대비 때문에 푼걸까요...? 풀려있네요)
T = int(input())
for t in range(T):
    N, P = map(int, input().split())
    # 우선순위 리스트 입력 받음
    ilist = list(map(int, input().split()))
    # 출력되는 순서를 표현하기 위한 변수
    cnt = 0
    # 우선 순위 리스트를 정렬 후 저장
    sorted_list = sorted(ilist)

    while True:
        # P는 현재 목표로 하는 대상의 위치의 index를 나타내는 변수
        # 만약 목표 index가 0보다 작다면 리스트 길이만큼 더해 마지막 index로 다시 설정
        if P < 0:
            P += len(ilist)
        # reverse를 하면 될텐데 그냥 풀었군요?
        # 가장 큰 값이 가장 앞에 있을 때
        if ilist[0] == sorted_list[-1]:
            # 출력 횟수 증가
            cnt += 1
            # 만약 목표 index가 현재 출력해야 하는 대상의 위치인 0이라면 break
            if P == 0:
                break
            # 목표 대상이 아니라면 각각의 리스트에서 출력 대상 제외
            sorted_list.pop()
            ilist.pop(0)
            # 항목이 줄어드므로 P도 1 감소
            P -= 1
        # 가장 큰 값이 가장 앞에 있지 않을 때
        else:
            # 첫번째 항목을 가장 마지막으로 보내고
            # 목표 index는 1 줄임
            ilist.append(ilist.pop(0))
            P -= 1

    print(cnt)