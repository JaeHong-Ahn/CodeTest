def change_k(n, k):
    ans = []
    st = ""
    while True:
        an = n % k
        ans.append(an)
        n //= k
        if n == 0:
            ans = ans.__reversed__()
            for a in ans:
                st += str(a)
            return st


def prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1/2))+1):
        if n % i == 0:
            return False

    return True

def solution(n, k):
    s = change_k(n, k)
    k = ""
    nums = []
    answer = 0

    for i in range(len(s)):
        if s[i] != '0':
            k += s[i]
            if i == len(s)-1:
                nums.append(k)
        elif s[i] == '0' and len(k) > 0:
            nums.append(k)
            k = ""

    for num in nums:
        if prime_num(int(num)):
            answer += 1

    return answer