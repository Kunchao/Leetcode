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

