T = int(input())

answer = 0

five = T // 5

three = (T % 5) / 3

while T >= 0:
    if T == 1 or T == 2 :
        answer = -1
        break

    # 5의 배수가 될때까지 3을 뺌
    if T // 5 == T / 5 :
        answer += (T // 5)
        break
    else :
        T -= 3
        answer += 1

print(answer)