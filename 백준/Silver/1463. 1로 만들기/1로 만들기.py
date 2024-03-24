T = int(input())

d = {1:0}

def recursion(T):
    if T in d.keys():
        return d[T]
    if T % 3 == 0 and T % 2 == 0:
        d[T] = min(recursion(T//3)+1, recursion(T//2)+1)

    elif T % 3 == 0:
        d[T] = min(recursion(T//3)+1, recursion(T-1) + 1)

    elif T % 2 == 0:
        d[T] = min(recursion(T//2) + 1, recursion(T-1) + 1)

    else :
        d[T] = recursion(T-1) + 1

    return d[T]

print(recursion(T))