def solution(money, K):
    money.sort(reverse=True)

    remaining = K
    answer = 0

    for m in money:
        answer += remaining // m
        remaining = remaining % m

    return answer

def run():
    N, K = map(int, input().split())
    money = [int(input()) for _ in range(N)]

    print(solution(money, K))

    return 0

if __name__ == "__main__":
    run()
