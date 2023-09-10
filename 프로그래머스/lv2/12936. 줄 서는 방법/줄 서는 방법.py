def solution(n, k):
    answer = []
    num = []
    for i in range(n):
        num.append(i + 1)
        # num = [1, 2, 3, 4]

    def mul(n):
        if n == 1:
            return n
        else:
            return n * mul(n - 1)

    # n이 2 이하일 경우
    if n == 2:
        if k == 1:
            return [1, 2]
        elif k == 2:
            return [2, 1]
    elif n == 1:
        return [1]
    # n이 3 이상일 경우
    else:
        li = []
        if k // mul(n + 1) == 1:
            for i in range(len(1, n + 1)):
                answer.append(n + 1 - i)

        else:
            for i in range(n-1, 0, -1):
                li.append((k-1) // mul(i))
                k %= mul(i)

            for k in range(len(li)):
                answer.append(num[li[k]])
                num.remove(num[li[k]])
            answer.append(num[0])
    return answer