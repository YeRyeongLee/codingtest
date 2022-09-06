MOVES = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

def biggest(N, board):
    maxval = 0

    for i in range(N):
        for j in range(N):
            maxval = max(maxval, board[i][j])
    

    return maxval


def move(N, board, dx, dy):
    newboard = [[0 for _ in range(N)] for _ in range(N)]

    # TODO: move함수 완성시키기
    # 지금은 어떻게 풀어야 할지 잘 모르겠다. 
    # 상하좌우 나눠서 풀 수 있을 것 같긴 한데
    # 그렇게 풀면 코드가 더러워질듯


    return newboard


def findMax(cnt, N, board):
    if cnt == 5:
        return biggest(N, board)
    
    candidates = []

    for dx, dy in MOVES:
        newboard = move(N, board, dx, dy)

        candidates.append(cnt+1, N, newboard)


    return max(candidates)


def solution(N, board):

    answer = findMax(0, N, board)

    return answer


def run():
    N = 3
    board = [
        [2, 2, 2],
        [4, 4, 4],
        [8, 8, 8],
    ]

    print(solution(N, board))

    return 0


if __name__ == "__main__":
    run()