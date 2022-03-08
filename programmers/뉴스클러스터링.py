import math

def inter_union(A, B):
    inter = 0
    union = 0
    
    ptr1 = 0
    ptr2 = 0
    
    while ptr1 < len(A) or ptr2 < len(B):
        if ptr1 >= len(A):
            union += 1
            ptr2 += 1
        elif ptr2 >= len(B):
            union += 1
            ptr1 += 1
        elif A[ptr1] == B[ptr2]:
            inter += 1
            union += 1
            ptr1 += 1
            ptr2 += 1
        elif A[ptr1] < B[ptr2]:
            union += 1
            ptr1 += 1
        else:
            union += 1
            ptr2 += 1
    
    if not union:
        inter, union = 1, 1
    return inter, union

def solution(str1, str2):
    answer = 0
    
    A = []
    B = []
    
    for i in range(len(str1)-1):
        new_str = str1[i:i+2].lower()
        
        if new_str.isalpha():
            A.append(new_str)
            
    for j in range(len(str2)-1):
        new_str = str2[j:j+2].lower()
        
        if new_str.isalpha():
            B.append(new_str)
    
    A.sort()
    B.sort()
    
    inter, union = inter_union(A, B)
    
    answer = math.floor(65536 * inter / union)
    
    return answer