# 스타트와 링크

N = int(input())

s = []

for _ in range(N):
    s.append(list(map(int, input().split())))

minimum = 1e9


def backtracking(k, start_team):
    global minimum

    if minimum == 0:
        return minimum

    if k == (N // 2):
        sum_start = 0
        sum_link = 0
        link_team = []

        for a in range(k - 1):
            for b in range(a + 1, k):
                sum_start += s[start_team[a]][start_team[b]] + s[start_team[b]][start_team[a]]

        for num in range(N):
            link_team.append(num)
            if num in start_team:
                link_team.pop()

        for c in range(k - 1):
            for d in range(c + 1, k):
                sum_link += s[link_team[c]][link_team[d]] + s[link_team[d]][link_team[c]]

        minimum = min(minimum, abs(sum_start - sum_link))

    else:
        for i in range(k, len(s)):
            if i in start_team:
                continue

            if len(start_team) != 0 and start_team[-1] >= i:
                continue

            start_team.append(i)
            backtracking(k + 1, start_team)
            start_team.pop()


backtracking(0, [])
print(minimum)
