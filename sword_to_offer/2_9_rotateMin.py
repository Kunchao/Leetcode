#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25
# @Author  : Vapor
# -*- coding:utf-8 -*-
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         # write code here
#         if len(rotateArray) == 0:
#             return 0
#         left, right = 0, len(rotateArray) - 1
#         while rotateArray[left] > rotateArray[right] and right - left > 1:
#             mid = (left + right) // 2
#             if rotateArray[mid] == rotateArray[left] == rotateArray[right]:
#                 self.minInOrder(rotateArray, left, right)
#             if rotateArray[mid] >= rotateArray[left]:
#                 left = mid
#             elif rotateArray[mid] <= rotateArray[right]:
#                 right = mid
#         return rotateArray[left] if rotateArray[left] < rotateArray[right] else rotateArray[right]
#
#     def minInOrder(self, arr, left, right):
#         result = arr[0]
#         for i in arr[left: right+1]:
#             if i < result:
#                 result = i
#         return result


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        left, right = 0, len(rotateArray) - 1
        while left < right:
            mid = (left + right) // 2
            # print(left, mid, right, rotateArray[left], rotateArray[mid], rotateArray[right])
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] == rotateArray[right]:
                right -= 1
            else:
                right = mid
        # print(left, mid, right)
        return rotateArray[right]


if __name__ == '__main__':
    a = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
    print(Solution().minNumberInRotateArray(a))