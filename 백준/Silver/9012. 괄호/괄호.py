T = int(input())

for test_case in range(T) :
    vps = list(input())

    answer = 0

    for v in vps :
        if answer < 0 :
            break

        if v == '(' :
            answer += 1
        elif v == ')' :
            answer -= 1

    if answer == 0 :
        print("YES")
    else :
        print("NO")
