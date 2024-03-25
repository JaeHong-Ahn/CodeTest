n = int(input())

ans = [1, 2, 4]

for i in range(n):
    num = int(input())
    if len(ans) >= num :
        print(ans[num-1])
    else :
        for j in range(num - len(ans)) :
            ans.append(sum(ans[len(ans)-3:]))

        print(ans[-1])