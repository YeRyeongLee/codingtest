from collections import deque


dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def inRange(x, y, tray):
    n = len(tray)
    m = len(tray[0])

    return x>=0 and x<n and y>=0 and y<m

def bfs(x, y, tray):
    tray[x][y] = 1

    que = deque()
    que.append((x, y))
    tray[x][y] = 1

    while que:
        x, y = que.pop()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if inRange(nx, ny, tray) and not tray[nx][ny]:
                que.append((nx, ny))
                tray[nx][ny] = 1
    

            




def solution(N, M, tray):
    answer = 0

    for i in range(N):
        for j in range(M):
            if not tray[i][j]:
                answer += 1
                bfs(i, j, tray)
    
    return answer


def run():
    N, M = map(int, input().split())

    tray = [
        input() for _ in range(N)
    ]

    newtray = [
        list(map(int, list(tray[i]))) for i in range(N)
    ]

    print(solution(N, M, newtray))

    return 0


if __name__ == "__main__":
    run()

