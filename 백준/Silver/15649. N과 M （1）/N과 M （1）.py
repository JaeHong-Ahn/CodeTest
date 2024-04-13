#N과 M

def recursion(num, arr):
    # global cnt

    if len(arr) == M:
        for k in range(len(arr)):
            print(arr[k], end=" ")
        print()
        return

    for i in range(1, N+1):
        if i in arr:
            continue
        arr.append(i)
        recursion(i, arr)
        arr.pop()

N,M = map(int, input().split())

nums = [i for i in range(1, N+1)]

recursion(0, [])