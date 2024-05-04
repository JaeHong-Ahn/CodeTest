import copy
from collections import deque


def bfs(check):
    global result
    global test_map

    q = deque()

    for c in range(len(check)):
        q.append((check[c][0], check[c][1]))

    while q:
        minus = 0
        r, c = q.popleft()

        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]

            if 0<= nr < M and 0 <= nc < N and graph[nr][nc] == 0 and test_map[nr][nc] == 0:
                q.append((nr, nc))
                test_map[nr][nc] = test_map[r][c] + 1
                result = max(result, test_map[nr][nc])

N, M = map(int, input().split())

graph = []
result = -1
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for _ in range(M):
    graph.append(list(map(int, input().split())))

test_map = copy.deepcopy(graph)

check = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            check.append([i, j])

bfs(check)

cnt = sum(row.count(0) for row in test_map)
cnt_1 = sum(row.count(1) for row in graph)
cnt_minus_1 = sum(row.count(-1) for row in graph)

if cnt > 0:
    print(-1)
elif (cnt_1 + cnt_minus_1) == (N*M):
    print(0)
else:
    print(result - 1)
