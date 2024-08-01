'''
나동빈 이코테
BFS 미로 탈출
'''

from collections import deque

maze = []
n, m = map(int, input().split())

for _ in range(n):
    maze.append(list(map(int,input())))

# 이동할 네 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):

    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 => 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우 => 무시
            if maze[nx][ny] == 0:
                continue

            # 처음 방문하는 경우에만 최단 경로 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx,ny))
    
    return maze[n-1][m-1]

print(bfs(0,0))


