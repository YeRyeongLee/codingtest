def make_cycle(grid, visited, i, j, d):
    length = 0
    
    d_dict = { # 방향바꾸기 매핑
        "S": 0,
        "L": -1,
        "R": +1,
    }
    direcs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 방향
    
    
    while not visited[i][j][d]:
        visited[i][j][d] = 1
        di, dj = direcs[d]
        i, j = (i + di) % len(grid), (j + dj) % len(grid[0])
        length += 1
        
        d = (d + d_dict[grid[i][j]]) % 4
    
    
    return length

def find_cycles(grid):
    cycles = []
    
    # 경로를 지났는지 체크 (순서 - 북, 동, 남, 서)
    visited = [[[0, 0, 0, 0] 
                for _ in range(len(grid[0]))] 
               for _ in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                if not visited[i][j][d]:
                    cycles.append(make_cycle(grid, visited, i, j, d))
    return cycles

def solution(grid):
    answer = []
    
    answer = find_cycles(grid)
    answer.sort()
    
    return answer