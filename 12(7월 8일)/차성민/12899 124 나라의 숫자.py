def solution(n):
    # 1,2,4로 만들 수 있는 총 경우 생각해보고 mod구별하여 값 넣어주기 -> 3으로 나눈거 보면 되네
    # 나머지 1 -> 1,  2 - > 2,  0 -> 4 (*주의 계산시에는 몫 1 빼줘야 함)

    answer = ''
    # dict 활용하여 나머지에 따른 값 넣어주기
    dict = {1: "1", 2: "2", 0: "4"}
    portion = 1
    remainder = 1

    # 몫이 0이 될 때까지 계산
    while portion != 0:
        portion = n // 3
        remainder = n % 3
        #나머지가 0일 떄, 4로 바꾸어주는 부분에서 몫을 1 뺴주어야 3단위로 싸이클이 맞음.
        if remainder == 0:
            portion -= 1
        n = portion
        # 기존 answer에 앞부분에 하나씩 숫자를 붙여서 만듦
        answer = dict[remainder] + answer

    return answer
