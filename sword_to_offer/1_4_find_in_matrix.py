#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/8
# @Author  : Vapor

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        col = len(array[0]) -1
        row = 0
        while col >= 0 and row < len(array):
            print(col, row)
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

# test exam
result = Solution().Find(1,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
print(result)