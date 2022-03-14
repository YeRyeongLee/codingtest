from collections import deque

def in_range(x, y, n, m):
    return x>=0 and x<n and y>=0 and y<m

def bfs(maps):
    Q = deque()
    n, m = len(maps), len(maps[0])
    END = n-1, m-1
    
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    visited[0][0] = 1
    Q.append((0, 0, 1))
    
    while Q:
        x, y, cnt = Q.popleft()
        
        if (x, y) == END:
            return cnt
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny, n, m) and maps[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                Q.append((nx, ny, cnt+1))
    
    return -1
                
    
def solution(maps):
    answer = 0
    
    answer = bfs(maps)
    
    return answer