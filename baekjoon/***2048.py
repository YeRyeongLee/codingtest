dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def maximum_number(board):
    maxi = 0
    for row in board:
        for val in row:
            if val > maxi:
                maxi = val
    
    return maxi


def in_range(n, nx, ny):
    return nx >= 0 and nx < n and ny >= 0 and ny < n

def move(n, board, dx, dy):
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    changed = [[0 for _ in range(n)] for _ in range(n)]

    dir = -(dx+dy)
    start = 0 if dir == 1 else n-1
    end = n if dir == 1 else -1

    for i in range(start, end, dir):
        for j in range(n):
            ni, nj = 0, 0
    return new_board



def find_maximum(n, board, moves):

    if moves == 0:
        return maximum_number(board)
    

    for dx, dy in zip(dxs, dys):
        new_board = move(board, dx, dy)
        maximums = []
        maximums.append(find_maximum(n, new_board, moves-1))
    
    return max(maximums)





if __name__ == "__main__":
    n = int(input())
    board = [[list(map(int, input().split()))] for _ in range(n)]

    print(find_maximum(n, board, 5))