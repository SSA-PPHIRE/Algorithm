'''
1. 오랜만에 찾아본 트리순회 알고리즘
def preorder(n):
    if n!=0:
        print(n, end=" ")
        preorder(child[n][0])
        preorder(child[n][1])

def inorder(n):
    if n!=0:
        inorder(child[n][0])
        print(n, end=" ")
        inorder(child[n][1])

def postorder(n):
    if n!=0:
        postorder(child[n][0])
        postorder(child[n][1])
        print(n, end=" ")

//
2. 완전이진트리면 풀이가 간단하다
1
23
4567
pre     : 뿌왼오 : 1245367
in      : 왼뿌오 : 4251637
post    : 왼오뿌 : 4526731

완전 이진트리인 경우 인오더만 사용해도 알 수 있음
뿌리를 찾아야 함
n//2 -> 뿌리
[0:n//2] [n//2+1:]

//
3. 완전 이진트리가 아니면 포스트오더도 같이 사용해야 함
1
23
456
pre : 뿌왼오 : 124536
in  : 왼뿌오 : 425163
post: 왼오뿌 : 452631

post의 마지막 -> 뿌리
in에서 root의 인덱스를 찾는다
post[:idx]가 왼쪽트리, post[idx:]가 오른쪽 트리

4.
구현했는데 뭐가 문제인지 제대로 작동하지 않는다
'''

n = 3
inval = [4,2,5,1,6,3]
postval = [4,5,2,6,3,1]

answer = []
def find_root(s,e):
    ans = postval[e-1]
    if s <= e and (ans not in answer):
        answer.append(ans)
        tmp = inval.index(ans)
        print(ans, s, e, '//', tmp, postval[s:tmp], postval[tmp:e-1])
        find_root(s,tmp)
        find_root(tmp,e-1)
    else:
        print('건너뜀')

find_root(0, len(postval))


print(*answer)

#########################################
n = 6
in_order = [4,2,5,1,6,3]
post_order = [4,5,2,6,3,1]


# in_order에서 in_order[i]의 인덱
pos = [0]*(n+1)
for i in range(n):
    pos[in_order[i]] = i

    
# 전위 순회
def divide(in_start, in_end, p_start, p_end):
    print(in_start, in_end, p_start, p_end)
    if(in_start > in_end) or (p_start > p_end):
        return

    parents = post_order[p_end] # 후위순회에서 부모노드 찾기
    print(parents)
    left = pos[parents] - in_start # in_order에서 왼쪽인자 갯수
    right = in_end - pos[parents] # in_order에서 오른쪽인자 갯수

    divide(in_start, in_start+left-1, p_start, p_start+left-1) # 왼쪽 노드
    divide(in_end-right+1, in_end, p_end-right, p_end-1) # 오른쪽 노드 divide(0, n-1, 0, n-1)

divide(0,n-1,0,n-1)
