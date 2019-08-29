#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24
# @Author  : Vapor
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(tin) == 0:
            return None
        root = TreeNode(pre.pop(0))
        rootIndex = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:rootIndex])
        root.right = self.reConstructBinaryTree(pre, tin[rootIndex + 1:])
        return root
        # root = self.constructBinaryTree(pre, 0, len(pre) - 1, tin, 0, len(tin) - 1)

    # def constructBinaryTree(self, pre, preStart, preEnd, tin, inStart, inEnd):
    #     if len(pre) == 0 | len(tin) == 0:
    #         return None

        # if len(pre) == 1:
        #     return TreeNode(pre[0])
        # root = TreeNode(preStart[preStart])
        # for i in range(inStart, inEnd):
        #     if preStart[preStart] == tin[i]:
        #         root.left = self.constructBinaryTree(pre, preStart + 1, preStart + i - 1, tin, 0, i )
        #         root.right = self.constructBinaryTree(pre, preStart + i, preEnd, tin, inStart + i + 1, inEnd)
