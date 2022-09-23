from collections import deque

def solution(N, connected):
    connected_dict = {}

    for i in range(1, N+1):
        connected_dict[i] = []

    for n1, n2 in connected:
        connected_dict[n1].append(n2)
        connected_dict[n2].append(n1)
    

    visited = [False for _ in range(N+1)]


    # bfs

    que = deque()
    que.append(1)
    visited[1] = True

    while que:
        curr_node = que.popleft()

        for next_node in connected_dict[curr_node]:
            if not visited[next_node]:
                que.append(next_node)
                visited[next_node] = True




    return sum(visited) - 1


def run():
    N = int(input())
    M = int(input())
    connected = [
        list(map(int, input().split())) for _ in range(M)
    ]

    print(solution(N, connected))

    return 0


if __name__ == "__main__":
    run()