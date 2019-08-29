#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15
# @Author  : Vapor


class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


root = node(5)
root.left = node(7)
root.right = node(8)
root.left.left = node(3)
root.left.right = node(4)
root.left.right.left = node(9)

stack = [root]


# 先序遍历，递归
def preOrderTraversed(node):
    if node is None:
        return None
    print(node.val)
    preOrderTraversed(node.left)
    preOrderTraversed(node.right)


def preOrder(node):
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        node = stack.pop()

# 中序遍历
def inOrderTraverse(node):
    if node is None:
        return None
    inOrderTraverse(node.left)
    print(node.val)
    inOrderTraverse(node.right)

def inOrder(node):
    stack = []
    pos = node
    while pos is not None or len(stack) > 0:
        if pos:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
            print(pos.val)
            pos = pos.right

# 后序遍历
def postOrderTraverse(node):
    if node is None:
        return None
    postOrderTraverse(node.left)
    postOrderTraverse(node.right)
    print(node.val)

# 借助辅助栈
def postOrder(node):
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.left:
            stack.append(node.left)
        # 注意是if
        if node.right:
            stack.append(node.right)
    while len(stack2) > 0:
        print(stack2.pop().val)

import queue
# 广度搜索
def layerTraverse(head):
    if not head:
        return None
    que = queue.Queue()
    que.put(head)
    while not que.empty():
        head = que.get()
        print(head.val)
        if head.left:
            que.put(head.left)
        if head.right:
            que.put(head.right)

#二叉树节点个数
def treeNodeCnt(node):
    if node is None:
        return 0
    nums = treeNodeCnt(node.left)
    nums += treeNodeCnt(node.right)
    return nums + 1

def maxDepthCnt(node):
    if node is None:
        return 0
    lCnt = maxDepthCnt(node.left)
    rCnt = maxDepthCnt(node.right)
    return max(lCnt, rCnt) + 1

if __name__ == '__main__':
    # print("前序遍历")
    # preOrderTraversed(root)
    # preOrder(root)
    # print("="*20)
    # print("中序遍历")
    # inOrderTraverse(root)
    # print("="*20)
    # inOrder(root)
    # print("后序遍历")
    # postOrder(root)
    # print("层次遍历")
    # layerTraverse(root)
    # print("二叉树节点个数:", treeNodeCnt(root))
    # print("最大深度:", maxDepthCnt(root))

