M, N = map(int, input().split())

def eratos(M, N):

    prime = [True] * (N + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(N**(1/2)+1)):
        if prime[i]:
            for j in range(i*2, N+1, i):
                prime[j] = False

    for k in range(M, N+1):
        if prime[k]:
            print(k)

eratos(M, N)