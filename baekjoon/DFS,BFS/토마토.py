from collections import deque

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

def in_range(x, y, N, M):
    return x>=0 and x<N and y>=0 and y<M


def findRipes(N, M, tomatoes):
    ripes = []

    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                ripes.append((i, j))

    return ripes

def unripeExists(tomatoes):
    exists = False


    for row in tomatoes:
        for elem in row:
            if elem == 0:
                exists = True


    return exists


def solution(N, M, tomatoes):

    ripes = findRipes(N, M, tomatoes)


    que = deque()

    for x, y in ripes:
        que.append((x, y, 0))
        tomatoes[x][y] = 1

    
    maxdist = 0
    

    while que:
        x, y, dist = que.popleft()
        maxdist = max(maxdist, dist)

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, N, M) and not tomatoes[nx][ny]:
                que.append((nx, ny, dist+1))
                tomatoes[nx][ny] = 1


    if unripeExists(tomatoes):
        answer = -1
    else:
        answer = maxdist
            
    
    return answer



def run():
    M, N = map(int, input().split())

    tomatoes = [
        list(map(int, input().split())) for _ in range(N)
    ]

    print(solution(N, M, tomatoes))

    return 0

if __name__ == "__main__":
    run()