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

result = 0
q = deque()

def bfs():
    global result

    while q:
        z, r, c = q.popleft()

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nz = z + dz[i]

            if 0 <= nr < M and 0<= nc < N and 0<= nz < H:
                if graph[nz][nr][nc] == 0:
                    graph[nz][nr][nc] = graph[z][r][c] + 1
                    q.append((nz,nr,nc))
                    result = max(result, graph[nz][nr][nc])

for i in range(H):
    for j in range(M):
        for k in range(N):
            if graph[i][j][k] == 1:
                q.append((i,j,k))

bfs()

done = True

cnt = 0
for i in range(H):
    for j in range(M):
        for k in range(N):
            if graph[i][j][k] == 0:
                done = False
            elif graph[i][j][k] == 1 or graph[i][j][k] == -1:
                cnt += 1

if cnt == (N*M*H):
    print(0)
elif done:
    print(result -1)
else:
    print(-1)
