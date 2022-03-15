def is_right(s):
    stack = []
    
    mapper = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    
    for c in s:
        if c in mapper:
            if stack and stack.pop() == mapper[c]:
                pass
            else:
                return False
        else:
            stack.append(c)
    
    if stack:
        return False
    else:
        return True

def shift(s):
    temp = s[0]
    new_s = ""
    
    for i in range(1, len(s)):
        new_s += s[i]
    
    return new_s + s[0]

def solution(s):
    answer = 0
    
    for _ in range(len(s)):
        s = shift(s)
        answer += int(is_right(s))
    
    return answer