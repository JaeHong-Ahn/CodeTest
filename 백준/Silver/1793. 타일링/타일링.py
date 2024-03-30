d = [0] * 251

while True:
    try:
        n = int(input())
        d[:2] = [1, 1, 3]
        for i in range(3, n + 1):
            d[i] = d[i - 1] + 2 * d[i - 2]
        print(d[n])
    except:
        break