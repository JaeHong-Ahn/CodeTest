def solution(tickets):

    answer = []

    visited = [False for _ in range(len(tickets))]

    # airport 출발지 찾음
    def find_start_airport(airport, visited):
        start = []
        for i in range(len(tickets)):
            if airport == tickets[i][0] and visited[i] == False:
                start.append(tickets[i])
        # 알파벳순 정렬
        start = sorted(start, key=lambda x: x[1])
        return start

    def dfs(previous, tickets, visited):

        #중복 값 체크
        loca = []
        for i in range(len(tickets)) :
            if tickets[i] == previous :
                loca.append(i)

        for i in range(len(loca)) :
            if visited[loca[i]] == False :
                visited[loca[i]] = True
                a.append(loca[i])
                answer.append(previous[1])
                break

        #탈출 조건
        if len(answer) == (len(tickets) + 1) and len(list(set(visited))) == 1:
            return answer

        if find_start_airport(previous[1], visited) == []:
            return False
        else:
            next = find_start_airport(previous[1], visited)

        for i in range(len(next)):

            if dfs(next[i], tickets, visited) :
                return answer

            answer.pop()
            visited[a[-1]] = False
            a.remove(a[-1])


    present = find_start_airport("ICN", visited)
    a = []
    answer = ["ICN"]
    for i in range(len(present)) :

        if dfs(present[i], tickets, visited) == False :
            answer = ["ICN"]
            visited = [False for _ in range(len(tickets))]
            continue
        else : dfs(present[i], tickets, visited)

    return answer