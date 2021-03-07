def solution(nums):
    new_nums = list(set(nums))

    if len(nums)/2 <= len(new_nums):
        return int(len(nums)/2)
    else:
        return int(len(new_nums))