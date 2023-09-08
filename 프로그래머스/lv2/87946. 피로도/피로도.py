def solution(k, dungeons):
    answer = []

    def recursion(k, cnt, visited, dungeons):
        for i in range(len(dungeons)):
            answer.append(cnt)
            if visited[i] == False and k >= dungeons[i][0]:
                visited[i] = True
                recursion(k-dungeons[i][1],cnt+1,visited, dungeons)
                visited[i] = False

        return answer
    visited = [False] * len(dungeons)
    recursion(k,0,visited,dungeons)

    return max(answer)