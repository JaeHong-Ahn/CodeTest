#숨바곡질
#bfs로도 구현해보기

A, B = map(int, input().split())

answer = 1e9

def recursion(A, B):
    if A >= B:
        return A - B
    if B == 1:
        return 1
    if B % 2:
        return 1 + min(recursion(A, B - 1),recursion(A, B + 1))

    return min(B - A, 1 + recursion(A, B // 2))

answer = recursion(A,B)

print(answer)