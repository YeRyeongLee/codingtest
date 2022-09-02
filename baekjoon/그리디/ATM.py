def solution(N, P):
    P.sort()

    answer = 0

    for i in range(N):
        answer += P[i] * (N-i)

    return answer

def run():
    N = int(input())
    P = list(map(int, input().split()))

    print(solution(N, P))

    return 0

if __name__ == "__main__":
    run()
