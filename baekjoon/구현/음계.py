

def solution(arr):
    answer = ""

    ascending = True
    descending = True


    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            descending = False
        elif arr[i-1] > arr[i]:
            ascending = False


    if ascending:
        answer = "ascending"
    elif descending:
        answer = "descending"
    else:
        answer = "mixed"


    return answer

def run():

    arr = list(map(int, input().split()))

    print(solution(arr))

    return 0

if __name__ == "__main__":
    run()