from collections import deque

def solution(land):
    n = len(land)  # 세로 길이
    m = len(land[0])  # 가로 길이
    
    # 방향 벡터: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        # BFS를 위한 큐 초기화
        queue = deque()
        queue.append((x, y))
        visit[x][y] = True
        mass = 0
        
        while queue:
            cx, cy = queue.popleft()
            mass += 1  # 석유 칸의 개수 증가
            
            # 네 방향으로 탐색
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                
                # 격자 범위 내에 있고, 석유가 있으며 방문하지 않은 칸인 경우
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True  # 방문 표시
                    queue.append((nx, ny))
        
        return mass
    
    max_oil = 0  # 최대 석유량 초기화
    
    # 각 열에 대해 탐색
    for col in range(m):
        total_oil = 0
        visit = [[False] * m for _ in range(n)]  # 방문 배열 초기화
        
        # 현재 열의 각 행에 대해 BFS 수행
        for row in range(n):
            if land[row][col] == 1 and not visit[row][col]:
                total_oil += bfs(row, col)  # 현재 열의 총 석유량 합산
        
        max_oil = max(max_oil, total_oil)  # 최대 석유량 갱신
    
    return max_oil  # 최대 석유량 반환

