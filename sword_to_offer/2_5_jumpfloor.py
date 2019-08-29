#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25
# @Author  : Vapor
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        result = [0, 1, 2]
        if number < 3:
            return result[number]
        jump_one = 1
        jump_two = 2
        fib = 0
        for i in range(2, number):
            fib = jump_one + jump_two
            jump_one = jump_two
            jump_two = fib
        return fib


if __name__ == '__main__':
    print(Solution().jumpFloor(4))