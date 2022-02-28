def is_decimal(num):
    dec = True
    for i in range(2, num):
        if num % i == 0:
            dec = False
    return dec


def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_decimal(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer