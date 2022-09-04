def solution(N, A, B):
    answer = 0

    sump = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(N):
        sump += A[i] * B[i]

    answer = sump
    
    return answer

def run():
    input1 = "5"
    input2 = "1 1 1 6 0"
    input3 = "2 7 8 3 1"

    N = int(input1)
    A = list(map(int, input2.split()))
    B = list(map(int, input3.split()))

    print(solution(N, A, B))

    return 0


if __name__ == "__main__":
    run()