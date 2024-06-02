# 스타트링크
from collections import deque

F, S, G, U, D = map(int, input().split())

ans = 0
v = [False] * (F + 1)

def bfs():
    global ans
    global v

    q = deque()

    q.append(S)

    while q:

        x = q.popleft()

        condition1 = (x + U) <= F
        condition2 = (x - D) > 0

        if x == G:
            break
        if abs(x + U - G) <= abs(x - D - G) and condition1 and not v[x + U]:
            q.append(x + U)
            v[x + U] = True
        elif condition2 and not v[x - D]:
            q.append(x - D)
            v[x - D] = True
        elif condition1 and not v[x + U]:
            q.append(x + U)
            v[x + U] = True
        else:
            ans = -1
            break

        ans += 1


bfs()

if ans == -1:
    print("use the stairs")
else:
    print(ans)