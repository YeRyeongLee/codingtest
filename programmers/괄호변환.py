def is_right(string):
    pairs = []
    
    for char in string:
        if char == ")":
            if not pairs:
                return False
            elif pairs[-1] == "(":
                pairs.pop()
            else:
                pairs.append(char)
        else:
            pairs.append(char)
    
    if pairs:
        return False
    else:
        return True

def make_it_right(string):
    if not string:
        return ""
    
    ptr = 0
    
    pair1 = 0
    pair2 = 0
    while ptr < len(string):
        
        if string[ptr] == "(":
            pair1 += 1
        else:
            pair2 += 1
            
        ptr += 1
        
        if pair1 == pair2:
            break
    
    u, v = string[:ptr], string[ptr:]
    
    if is_right(u):
        return u + make_it_right(v)
    else:
        temp = "(" + make_it_right(v) + ")"
        
        new_u = ""
        for i in range(1, len(u)-1):
            if u[i] == "(":
                new_u += ")"
            else:
                new_u += "("
        
        return temp + new_u
        
        

def solution(p):
    answer = make_it_right(p)
    
    return answer