#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18
# @Author  : Vapor


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        mergeList = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                mergeList.append(nums1[i])
                i += 1
            elif nums1[i] >= nums2[j]:
                mergeList.append(nums2[j])
                j += 1
        mergeList = mergeList + nums1[i:] + nums2[j:]
        if len(mergeList) % 2 == 1:
            return mergeList[len(mergeList)//2]
        else:
            mid = len(mergeList)//2 - 1
            return (mergeList[mid] + mergeList[mid + 1])/2


if __name__ == '__main__':
    l1 = [1,3]
    l2 = [2,4]
    print(Solution().findMedianSortedArrays(l1, l2))