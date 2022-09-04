
def makeList(expression):

    expList = []
    numStr = ""

    for char in expression:
        if char in ["+", "-"]:
            expList.append(int(numStr))
            expList.append(char)
            numStr = ""
        else:
            numStr += char
    
    expList.append(int(numStr))

    return expList


def solution(expression):
    answer = 0

    expList = makeList(expression)

    findMinus = False

    for exp in expList:
        if exp == '-':
            findMinus = True
        elif exp == '+':
            pass
        elif findMinus:
            answer -= exp
        else:
            answer += exp


    return answer

def run():
    expression = "00009-00009"

    print(solution(expression))

    return 0


if __name__ == "__main__":
    run()


    