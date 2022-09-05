def R(s, e, dir, error):
    return s, e, -dir, error

def D(s, e, dir, error):
    if dir == 1:
        s += 1
    else:
        e -= 1

    if s > e:
        error = True
    
    return s, e, dir, error


FUNC = {
    "R": R,
    "D": D,
}


def solution(p, n, arr):
    answer = ""

    s, e = 0, n
    dir = 1
    error = False

    for char in p:
        s, e, dir, error = FUNC[char](s, e, dir, error)
    
    if error:
        answer = "error"
    else:
        newArr = []
        if dir == 1:
            for i in range(s, e):
                newArr.append(str(arr[i]))
        else:
            for i in range(e-1, s-1, -1):
                newArr.append(str(arr[i]))

        answer = "[" + ",".join(newArr) + "]"

    return answer


def run():
    T = int(input())

    for _ in range(T):
        p = input()
        n = int(input())

        # exception
        if not n:
            rawArr = input()
            if "D" in p:
                print("error")
            else:
                print("[]")
            continue

        rawArr = input()
        arr = list(map(int, rawArr[1:-1].split(",")))
        
        print(solution(p, n, arr))

    return 0

if __name__ == "__main__":
    run()