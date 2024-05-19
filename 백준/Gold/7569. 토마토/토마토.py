from collections import deque

N, M, H = map(int, input().split())

graph = []

dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

for _ in range(H):
    floors = []
    for _ in range(M):
        floors.append(list(map(int, input().split())))
    graph.append(floors)
    del floors

result = 0
q = deque()

def bfs():
    global result

    while q:
        z, r, c, a = q.popleft()

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nz = z + dz[i]

            if 0 <= nr < M and 0<= nc < N and 0<= nz < H:
                if graph[nz][nr][nc] == 0:
                    graph[nz][nr][nc] = a + 1
                    q.append((nz,nr,nc,a+1))

    answer = -1
    for z in range(len(graph)):
        for r in range(len(graph[0])):
            for c in range(len(graph[0][0])):
                if graph[z][r][c] == 0:
                    return -1
                answer = max(answer, graph[z][r][c])

    return answer - 1

for i in range(H):
    for j in range(M):
        for k in range(N):
            if graph[i][j][k] == 1:
                q.append((i,j,k, 1))

print(bfs())
