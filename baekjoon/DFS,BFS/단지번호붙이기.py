from collections import deque


dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def inRange(x, y, N):
    return x>=0 and x<N and y>=0 and y<N

def bfs(N, x, y, maps):
    cnt = 0
    maps[x][y] = 0

    que = deque()
    que.append((x, y))

    while que:
        x, y = que.pop()
        cnt += 1

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if inRange(nx, ny, N) and maps[nx][ny]:
                maps[nx][ny] = 0
                que.append((nx, ny))

    return cnt

def solution(N, maps):
    houses = []

    for i in range(N):
        for j in range(N):
            if maps[i][j]:
                houses.append(bfs(N, i, j, maps))
    
    houses.sort()

    return houses


def run():
    N = int(input())
    maps = [
        list(map(int, list(input()))) for _ in range(N)
    ]

    houses = solution(N, maps)

    print(len(houses))

    for h in houses:
        print(h)

    return 0


if __name__ == "__main__":
    run()
