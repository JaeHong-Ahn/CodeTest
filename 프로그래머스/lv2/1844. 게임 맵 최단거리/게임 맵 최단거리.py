from collections import deque


def solution(maps):
    answer = 0

    if bfs(0, 0, maps) == 1:
        return -1
    else:
        answer = bfs(0, 0, maps)

    return answer


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, maps):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            elif maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return maps[len(maps) - 1][len(maps[0]) - 1]