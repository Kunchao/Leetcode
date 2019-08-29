#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/16
# @Author  : Vapor


def binarySearch(arr, val):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return True
        elif val < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False


class BSTNode:
    # initial a tree
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self.root is None

    def search(self, key):
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry:
                bt = bt.left
            elif key > entry:
                bt = bt.right
        return None

    def insert(self, key):
        bt = self._root
        if not bt:
            return None
        while True:
            entry = bt.node
            if key < entry:
                if bt.left is None:
                    bt.left = BSTNode(key)
                bt = bt.left
            elif key > bt.node:
                if bt.right is None:
                    bt.right = BSTNode(key)
                bt = bt.right
            else:
                bt.data = key




