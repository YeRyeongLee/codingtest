def solution(N, M, cards):
    answer = 0

    mins = []

    for i in range(N):
        mins.append(min(cards[i]))

    answer = max(mins)

    return answer


def run():
    input1 = "3 3"
    inputs = ["3 1 2", "4 1 4", "2 2 2"]

    N, M = map(int, input1.split())
    cards = [list(map(int, inputs[i].split())) for i in range(N)]

    print(solution(N, M, cards))

    return 0

if __name__ == "__main__":
    run()
