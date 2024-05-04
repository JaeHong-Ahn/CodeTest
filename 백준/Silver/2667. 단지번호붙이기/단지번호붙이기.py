from collections import deque

def bfs(i, j):
    global blocks
    global cnt

    count = 0

    if graph[i][j] == 1:

        q = deque()
        q.append((i, j))

        while q:
            i, j = q.popleft()

            for a in range(4):
                nr = i + dr[a]
                nc = j + dc[a]

                if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == 1:
                    q.append((nr,nc))
                    graph[nr][nc] += 1
                    count += 1

            if count == 0:
                count = 1

        blocks += 1
        cnt.append(count)

N = int(input())

graph = []
blocks = 0
cnt = []

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for _ in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        bfs(i, j)

print(blocks)
for c in sorted(cnt):
    print(c)
