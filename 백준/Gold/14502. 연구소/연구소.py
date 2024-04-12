from collections import deque

N, M = map(int, input().split())

labs = []
result = 0

for _ in range(N):
    labs.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    que = deque()
    test_map = [row[:] for row in labs]

    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 2:
                que.append((i, j))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if test_map[nx][ny] == 0:
                    test_map[nx][ny] = 2
                    que.append((nx, ny))

    cnt = sum(row.count(0) for row in test_map)
    global result
    result = max(result, cnt)

def wall(start_x, start_y, cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(start_x, N):
        for j in range(start_y if i == start_x else 0, M):
            if labs[i][j] == 0:
                labs[i][j] = 1
                wall(i, j, cnt + 1)
                labs[i][j] = 0

wall(0, 0, 0)

print(result)
