def make_tuple(tup_mat):
    tup = []
    i = 1
    
    while tup_mat[i]:
        for elem in tup_mat[i]:
            if elem not in tup:
                tup.append(elem)
        
        i += 1
    
    return tup

def split(s):
    tup_mat = [[] for _ in range(502)]
    new_s = s[1:-1]
    
    temp = ""
    
    for c in new_s:
        if c == "}":
            if temp[0] == ',':
                temp = temp[1:]
            lst = list(map(int, temp.split(sep=',')))
            tup_mat[len(lst)] = lst
            temp = ""
        elif c == "{":
            pass
        else:
            temp += c
    return tup_mat

def solution(s):
    answer = []
    
    tup_mat = split(s)
    
    answer = make_tuple(tup_mat)
    
    return answer