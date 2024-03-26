# 바이러스

N = int(input())

L = int(input())

graph = [[] * (N + 1) for _ in range(N + 1)]

for i in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)

cnt = 0


def recursion1(n):
    global cnt
    visited[n] = 1

    for i in graph[n]:
        if (visited[i] == 0):
            recursion1(i)
            cnt += 1

recursion1(1)
print(cnt)