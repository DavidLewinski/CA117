#!/usr/bin/env python3

def minimum(nums):
    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[1]:
        del(nums[1])
    else:
        del(nums[0])
    return (minimum(nums))
