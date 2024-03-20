#소수 구하기

M, N = map(int, input().split())

for i in range(M, N+1) :
    if i == 1 :
        continue
    half = pow(i, 1/2)
    for j in range(2, int(half)+1) :
        if i % j == 0 :
            break
    else :
        print(i)
