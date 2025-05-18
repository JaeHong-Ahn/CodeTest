def solution(n, t, m, p):
    answer = ''
    max = (m * (t-1) + p) # 최대 몇번째까지 구해야 하는지
    allNum = '0'
    nowNum = 1
    while(len(allNum) < max):
        allNum += changeNum(nowNum, n)
        nowNum += 1
    for i in range(t):
        answer += allNum[(p-1)+(m*i)]
    return answer

def changeNum(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod == 10:
            mod = 'A'
        elif mod == 11:
            mod = 'B'
        elif mod == 12:
            mod = 'C'
        elif mod == 13:
            mod = 'D'
        elif mod == 14:
            mod = 'E'
        elif mod == 15:
            mod = 'F'
        rev_base += str(mod)

    return rev_base[::-1]