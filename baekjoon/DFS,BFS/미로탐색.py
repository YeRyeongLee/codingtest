from collections import deque

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

def inRange(x, y, maze):
    n = len(maze)
    m = len(maze[0])

    return x>=0 and x<n and y>=0 and y<m

def solution(N, M, maze):
    answer = 0

    canMove = [list(map(int, list(maze[i]))) for i in range(len(maze))]

    que = deque()
    que.append((0, 0, 1))
    canMove[0][0] = 0

    while que:
        x, y, dist = que.popleft()

        if (x, y) == (N-1, M-1):
            answer = dist
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if inRange(nx, ny, maze) and canMove[nx][ny]:
                que.append((nx, ny, dist+1))
                canMove[nx][ny] = 0

    return answer


def run():
    N, M = map(int, input().split())
    maze = [
        input() for _ in range(N)
    ]

    print(solution(N, M, maze))

    return 0


if __name__ == "__main__":
    run()