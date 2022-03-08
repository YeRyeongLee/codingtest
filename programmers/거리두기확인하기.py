from collections import deque

ROW = 5
COL = 5
PLC = 5
THRESHOLD = 2
DIST_MAX = 25

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

def in_range(x, y):
    return x >= 0 and x < ROW and y >= 0 and y < COL

def check(place, visited, x, y):
    # 다른 면접자와의 맨하튼 거리의 최솟값 반환
    visited[x][y] = 1
    
    dists = [DIST_MAX]
    
    Q = deque()
    Q.append((x, y, 0))
    
    while Q:
        x, y, dist = Q.popleft()
        
        if place[x][y] == "P":
            if dist:
                dists.append(dist)
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and not visited[nx][ny]:
                if place[nx][ny] != "X":
                    visited[nx][ny] = 1
                    Q.append((nx, ny, dist+1))
    
    return min(dists)
    
def is_safe(place):
    
    for i in range(ROW):
        for j in range(COL):
            if place[i][j] == 'P':
                visited = [[0 for _ in range(COL)] for _ in range(ROW)]
                dist = check(place, visited, i, j)
                
                if dist <= THRESHOLD:
                    return 0
    
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(is_safe(place))
    return answer