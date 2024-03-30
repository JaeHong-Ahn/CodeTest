# 바이러스
# visited 없이도 풀어보기

N = int(input())

L = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(L):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

ans = []

def recursion_no_visited(i):
    for j in range(1, N+1):
        if graph[i][j] == 1:
            graph[i][j] += 1
            graph[j][i] += 1
            if i not in ans:
                ans.append(i)
            if j not in ans:
                ans.append(j)

            recursion_no_visited(j)
    return ans

if L == 0:
    print(0)
else:
    print(len(recursion_no_visited(1))-1)