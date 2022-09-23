from collections import deque


def dfs(V, adjacent, visited, order):
    stack = deque()
    stack.append(V)

    while stack:
        curr = stack.pop()

        if not visited[curr]:
            order.append(curr)
            visited[curr] = 1

            for i in range(len(adjacent[curr])-1, -1, -1):
                next = adjacent[curr][i]
                stack.append(next)


def bfs(V, adjacent, visited, order):
    que = deque()
    que.append(V)
    visited[V] = 1
    order.append(V)

    while que:
        curr = que.popleft()
        


        for node in adjacent[curr]:
            if not visited[node]:
                que.append(node)
                visited[node] = 1
                order.append(node)



def printlst(lst):
    newlst = list(map(str, lst))
    print(" ".join(newlst))


def solution(N, M, V, edges):
    adjacent = [[] for _ in range(N+1)]

    for n1, n2 in edges:
        adjacent[n1].append(n2)
        adjacent[n2].append(n1)
    

    # 진짜 어이없는 거에서 실수함;; range(N)까지 정렬함...ㅜ
    for i in range(N+1):
        adjacent[i].sort()
    
    visited = [0 for _ in range(N+1)]
    order_dfs = []
    dfs(V, adjacent, visited, order_dfs)

    visited = [0 for _ in range(N+1)]
    order_bfs = []
    bfs(V, adjacent, visited, order_bfs)

    printlst(order_dfs)
    printlst(order_bfs)


def run():
    N, M, V = map(int, input().split())
    edges = [
        list(map(int, input().split())) for _ in range(M)
    ]

    solution(N, M, V, edges)

    return 0


if __name__ == "__main__":
    run()