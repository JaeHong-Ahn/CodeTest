# 아기 상어
from collections import deque

def bfs(si, sj):
    # [1] 필요한 자료형 생성
    q = deque()
    v = [[0]*N for _ in range(N)]
    tlst = []

    # [2] q에 초기데이터(들) 삽입, v 방문 표시
    q.append((si,sj))
    v[si][sj] = 1
    eat = 0

    while q:
        ci, cj = q.popleft()
        # eat == v[ci][cj]      #eat에 적힌 거리는 모두 list에 넣었음 -> 방문
        if eat == v[ci][cj]:
            return tlst, eat-1

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and shark >=arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                #나보다 작은 물고기인 경우 -> tlist에 추가
                if shark > arr[ni][nj] > 0:
                    tlst.append((ni,nj))
                    eat = v[ni][nj]
    #방문을 모두 끝낸 경우 -> 먹을 물고기를 못찾은 경우
    return tlst, eat-1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            ci, cj = i, j
            arr[i][j] = 0

shark = 2
cnt = ans = 0

while True:
    tlst, dist = bfs(ci, cj)
    if len(tlst) == 0:
        break
    tlst.sort(key = lambda x: (x[0], x[1]))
    ci, cj = tlst[0]
    arr[ci][cj] = 0     #물고기 먹음
    cnt += 1
    ans += dist
    if shark == cnt:
        shark += 1
        cnt = 0

print(ans)