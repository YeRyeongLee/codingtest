def shift(alph):
    return min((ord(alph) - ord('A')) % 26, (ord('A') - ord(alph)) % 26)

def move(done, ptr):
    right = ptr
    left = ptr
    
    r_move = 0
    l_move = 0
    
    while done[right]:
        right = (right + 1) % len(done)
        r_move += 1
    
    while done[left]:
        left = (left - 1) % len(done)
        l_move += 1
    
    if r_move <= l_move:
        return right, r_move
    else:
        return left, l_move

def solution(name):
    answer = 0
    
    done = [0 for _ in range(len(name))]
    
    for i, c in enumerate(name):
        if c == "A":
            done[i] = 1
    
    all_done = sum(done) == len(name)
    
    ptr = 0
    while not all_done:
        answer += shift(name[ptr])
        done[ptr] = 1
        
        
        all_done = sum(done) == len(name)
        if all_done:
            break
        
        ptr, dist = move(done, ptr)
        answer += dist
    
    return answer