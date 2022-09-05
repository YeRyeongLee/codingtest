DIRS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

def inRange(N, x, y):
    return x>=1 and x<=N and y>=1 and y<=N

def solution(N, moves):
    answer = 0, 0

    x, y = 1, 1

    for move in moves:
        dx, dy = DIRS[move]

        nx, ny = x + dx, y + dy

        if inRange(N, nx, ny):
            x, y = nx, ny
    
    answer = x, y

    return answer

def run():
    N = 5
    moves = ['R', 'R', 'R', 'U', 'D', 'D']

    print(solution(N, moves))

    return 0

if __name__ == "__main__":
    run()