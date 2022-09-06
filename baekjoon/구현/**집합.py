
def docmd(cmd, x, S):
    if cmd == "add":
        S[x] = 1
    elif cmd == "remove":
        if x in S:
            S[x] = 0
    elif cmd == "check":
        if x in S:
            print(S[x])
        else:
            print(0)
    elif cmd == "toggle":
        if x in S:
            if S[x]:
                S[x] = 0
            else:
                S[x] = 1
        else:
            S[x] = 1
    elif cmd == "all":
        newS = {}
        for i in range(1, 21):
            newS[i] = 1
        S = newS
    else:
        S = {}
    

def run():
    M = int(input())

    S = {}

    for _ in range(M):
        cmd, num = input().split()
        num = int(num)

        docmd(cmd, num, S)
    
    return 0


if __name__ == "__main__":
    run()


