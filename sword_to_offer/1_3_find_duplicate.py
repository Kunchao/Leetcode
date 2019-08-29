#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/8
# @Author  : Vapor


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        for k, num in enumerate(numbers):
            while k != num:
                if num == numbers[num]:
                    duplication[0] = num
                    return True
                else:
                    numbers[k], numbers[num] = numbers[num], numbers[k]
                    num = numbers[k]
        duplication[0] = -1
        return False


class Solution:
    """
    数组中重复的数字，不能修改数组
    """
    def countRange(self, nums, i, j) -> int:
        return sum(i <= v <= j for v in nums)

    def duplicate(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = len(nums) // 2 + start
            cnt = self.countRange(nums=nums, i=start, j=mid)
            if start == end:
                if cnt > 1:
                    return start
                else:
                    break
            if cnt > mid - start + 1:
                end = mid
            else:
                start = mid + 1
        return -1





