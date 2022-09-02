def solution(N, M, K, arr):

    answer = 0

    arr.sort(reverse=True)

    for i in range(M):
        if (i+1) % (K+1) == 0:
            answer += arr[1]
        else:
            answer += arr[0]

    return answer


def run():
    input1 = "5 8 3"
    input2 = "2 4 5 4 6"

    N, M, K = map(int, input1.split())
    arr = list(map(int, input2.split()))

    answer = solution(N, M, K, arr)

    print(answer)

    return answer


if __name__ == "__main__":
    run()