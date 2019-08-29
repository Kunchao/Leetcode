#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24
# @Author  : Vapor

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        # 中序
        next = None
        if pNode is None:
            return None
        if pNode.right != None:
            pRight = pNode.right
            while pRight.left != None:
                pRight = pRight.left
            next = pRight
        elif pNode.next != None:
            pCurrent = pNode
            nParent = pNode.next
            while nParent and pCurrent == nParent.right:
                pCurrent = nParent
                nParent = nParent.next
            next = nParent
        return next




