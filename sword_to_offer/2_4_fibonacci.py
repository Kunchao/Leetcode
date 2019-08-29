#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25
# @Author  : Vapor

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 1:
            return 0
        if n == 2:
            return 1
        return self.Fibonacci(n-1) + self.Fibonacci(n - 2)


class Solution:
    def Fibonacci(self, n):
        # write code here
        result = [0, 1]
        if n < 2:
            return result[n]

        fib_minus_one = 1
        fib_minus_two = 0
        fib = 0
        for i in range(2, n+1):
            fib = fib_minus_one + fib_minus_two
            fib_minus_two = fib_minus_one
            fib_minus_one = fib
        return fib

if __name__ == '__main__':
    print(Solution().Fibonacci(2))
