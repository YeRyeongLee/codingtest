from collections import deque

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

def in_range(x, y, cabbage):
    n = len(cabbage)
    m = len(cabbage[0])

    return x>=0 and x<n and y>=0 and y<m

def bfs(n, m, visited, cabbage):
    que = deque()

    que.append((n, m))
    visited[n][m] = 1


    while que:
        x, y = que.popleft()

        for dx, dy in zip(dxs, dys):

            nx, ny = x + dx, y + dy

            if in_range(nx, ny, cabbage) and cabbage[nx][ny] and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = 1
    





def solution(M, N, K, locations):
    answer = 0

    visited = [[0 for _ in range(M)] for _ in range(N)]
    cabbage = [[0 for _ in range(M)] for _ in range(N)]

    for m, n in locations:
        cabbage[n][m] = 1
    

    for m, n in locations:
        if not visited[n][m]:
            visited[n][m] = 1
            bfs(n, m, visited, cabbage)
            answer += 1

    return answer

def run():
    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())

        locations = [
            list(map(int, input().split())) for _ in range(K)
        ]

        print(solution(M, N, K, locations))

    return 0


if __name__ == "__main__":
    run()

        