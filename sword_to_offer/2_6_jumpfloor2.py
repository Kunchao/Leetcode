#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25
# @Author  : Vapor
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        result = [0, 1]
        if number < 2:
            return result[number]
        if number >= 2:
            return 2 * self.jumpFloorII(number - 1)


if __name__ == '__main__':
    print(Solution().jumpFloorII(5))
