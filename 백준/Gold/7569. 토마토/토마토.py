from collections import deque

N, M, H = map(int, input().split())

graph = []

dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

cnt_one = 0
cnt_minus_one = 0
for _ in range(H):
    floors = []
    for _ in range(M):
        floors.append(list(map(int, input().split())))
    cnt_one += sum(row.count(1) for row in floors)
    cnt_minus_one += sum(row.count(-1) for row in floors)
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

    for h in graph:
        for n in h:
            if 0 in n:
                return -1

    if (cnt_one + cnt_minus_one) == (N*M*H):
        return 0

    return result -1

for i in range(H):
    for j in range(M):
        for k in range(N):
            if graph[i][j][k] == 1:
                q.append((i,j,k))

print(bfs())
