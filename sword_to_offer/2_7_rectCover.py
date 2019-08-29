#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25
# @Author  : Vapor
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        result = [0, 1]
        if number < 2:
            return result[number]
        n1 = 1
        n2 = 1
        fib = 0
        for i in range(2, number+1):
            fib = n1 + n2
            n1 = n2
            n2 = fib
        return fib


if __name__ == '__main__':
    print(Solution().rectCover(5))

