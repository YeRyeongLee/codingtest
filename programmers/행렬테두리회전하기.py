import sys
INT_MAX = sys.maxsize

direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def shift_and_findmin(grid, x, y, w, h):
    dist = [w, h, w, h]
    prev = grid[x][y]
    temp = 0
    min_ = INT_MAX
    for (dx, dy), n in zip(direcs, dist):
        for i in range(1, n):
            min_ = min(min_, prev)
            
            nx, ny = x + dx * i, y + dy * i
            
            temp = grid[nx][ny]
            grid[nx][ny] = prev
            prev = temp
        
        x, y = nx, ny
    
    return min_


def solution(rows, columns, queries):
    answer = []
    
    grid = [[columns * i + j + 1 for j in range(columns)] for i in range(rows)]
    
    for q in queries:
        x, y, x2, y2 = tuple(q)
        w, h = y2-y + 1, x2-x + 1
        x, y = x-1, y-1
        answer.append(shift_and_findmin(grid, x, y, w, h))
    
    return answer