# a^b의 1의 자리 숫자 구하기

NUMDICT = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

def solution(a, b):
    answer = 0

    a = a % 10

    b = (b-1) % len(NUMDICT[a])

    if a == 0:
        answer = 10
    else:
        answer = NUMDICT[a][b]

    return answer


def run():
    T = int(input())

    for _ in range(T):
        a, b = map(int, input().split())

        print(solution(a, b))
    
    return 0


if __name__ == "__main__":
    run()