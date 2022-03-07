ops = []

def can_be_target(numbers, target):
    calc = 0
    for num, op in zip(numbers, ops):
        calc += num * op
    
    if calc == target:
        return 1
    else:
        return 0

def find_target(numbers, target):
    if len(ops) == len(numbers):
        return can_be_target(numbers, target)
    
    num_of_cases = 0
    for op in [+1, -1]:
        ops.append(op)
        num_of_cases += find_target(numbers, target)
        ops.pop()
    
    return num_of_cases


def solution(numbers, target):
    answer = find_target(numbers, target)
    return answer