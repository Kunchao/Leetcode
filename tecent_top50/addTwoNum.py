#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17
# @Author  : Vapor


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re: ListNode = ListNode(0)
        r = re
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10
            s = s % 10
            r.next = ListNode(s)
            r = r.next
            if l1!=None: l1 = l1.next
            if l2!=None: l2 = l2.next
        if carry > 0:
            r.next = ListNode(1)
        print(r.val)
        while re.next:
            print(re.next.val)
            re = re.next
        return re.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    Solution().addTwoNumbers(l1, l2)


