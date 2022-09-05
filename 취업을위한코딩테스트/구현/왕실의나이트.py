MOVES = [
    (2, -1),
    (2, 1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
]

def inRange(x, y):
    return x>=1 and x<=8 and y>=1 and y<=8

def solution(loc):
    answer = 0

    row = int(loc[1])
    col = ord(loc[0])-ord("a") + 1

    for dx, dy in MOVES:
        nx, ny = row + dx, col + dy

        if inRange(nx, ny):
            answer += 1


    return answer


def run():
    loc = "a1"

    print(solution(loc))

    return 0


if __name__ == "__main__":
    run()
