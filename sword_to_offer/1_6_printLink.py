#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24
# @Author  : Vapor
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        head = listNode
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
