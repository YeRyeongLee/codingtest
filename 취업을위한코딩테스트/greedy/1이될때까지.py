def solution(N, K):
    answer = 0

    cnt = 0

    while N != 1:
        if N % K == 0:
            N = N // K
        else:
            N -= 1
        cnt += 1

    answer = cnt

    return answer


def run():
    input1 = "25 3"

    N, K = map(int, input1.split())

    print(solution(N, K))

    return 0

if __name__ == "__main__":
    run()
