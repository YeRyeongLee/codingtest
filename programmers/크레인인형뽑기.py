def solution(board, moves):
    answer = 0
    
    stack = []
    
    for move in moves:
        i = 0
        j = move-1
        while i < len(board) and not board[i][j]:
            i += 1
        
        if i == len(board):
            break
        
        if stack and stack[-1] == board[i][j]:
            stack.pop()
            answer += 2
        else:
            stack.append(board[i][j])
        
        board[i][j] = 0
        
        
        
    
    return answer