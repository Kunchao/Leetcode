#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24
# @Author  : Vapor
# -*- coding:utf-8 -*-


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        if node:
            self.stack1.append(node)

    def pop(self):
        if len(self.stack2) > 0:
            return self.stack2.pop()
        else:
            while len(self.stack1) > 0:
                pop_value = self.stack1.pop()
                self.stack2.append(pop_value)
            return self.stack2.pop()


if __name__ == '__main__':
    op = Solution()
    op.push(1)
    op.push(2)
    op.push(3)
    # print(op.stack1)
    print(op.pop())
    print(op.pop())
    op.push(4)
    # print(op.stack1)
    print(op.pop())
    op.push(5)
    print(op.pop())
    # print(op.stack1)
    # print(op.stack2)