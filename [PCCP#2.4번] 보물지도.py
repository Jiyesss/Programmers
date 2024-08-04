from collections import deque

def solution(n, m, hole):
    answer = 0
    dx = [-1,1,0,0] # 이동 범위
    dy = [0,0,-1,1]
  
    
    
    def bfs(x,y,answer):
        magic = 0 # 신비시발 미사용: 0, 신비신발 사용: 1
        q = deque()
        q.append((x,y))
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                
                nx = x + dx[i]
                ny = y + dy[i]
                
                a = [nx,ny]
                if 1 <= nx < n and 1 <= ny < m and a not in hole:
                    
                    if magic == 0:
                        answer += 1
                        if nx != x:
                            q.append((x + 2* dx[i],ny))
                            magic += 1
                        elif ny != y :
                             q.append((nx, y+ 2*dy[i]))
                             magic += 1
                    
                    else: 
                        answer += 1
                        q.append((nx,ny))
                    
            if x==n-1 and y==m-1:
                return answer

        return -1
                            
        
        
    return bfs(1,1,answer)

solution(4,4,[[2, 3], [3, 3]])