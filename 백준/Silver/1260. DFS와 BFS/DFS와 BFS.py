from collections import deque

#N = 정점의 개수
#M = 간선의 개수
#V = 시작할 정점의 번호
N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)  # dfs의 방문기록
visited2 = [False] * (N + 1)  # bfs의 방문기록

def dfs(V):
    visited1[V] = True
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visited1[i] and graph[V][i]:
            dfs(i)

def bfs(V):
    q = deque([V])
    visited2[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if not visited2[i] and graph[V][i]:
                q.append(i)
                visited2[i] = True

dfs(V)
print()
bfs(V)