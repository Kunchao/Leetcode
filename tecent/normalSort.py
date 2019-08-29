#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15
# @Author  : Vapor


# 冒泡排序
def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 选择排序
def selectSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

# 插入排序
def insertSort(arr):
    for i in range(0, len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex > 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current

# shell 排序
def shellSort(arr):
    n = len(arr)
    gap = n//3
    while gap > 0:
        for i in range(gap, n):
            curNum, preIndex = arr[i], i - gap
            while preIndex >= 0 and curNum > arr[preIndex]:
                arr[i] = arr[preIndex]
                preIndex -= gap
            arr[preIndex + gap] = curNum
        gap //= 3
    return arr


# 归并排序
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    print(left, right)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    print(left[i:], right[j:])
    result = result + left[i:] + right[j:]
    return result


# def mergeSort(nums):
#     # 归并过程
#     def merge(left, right):
#         result = []  # 保存归并后的结果
#         i = j = 0
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#         result = result + left[i:] + right[j:] # 剩余的元素直接添加到末尾
#         return result
#     # 递归过程
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) // 2
#     left = mergeSort(nums[:mid])
#     right = mergeSort(nums[mid:])
#     return merge(left, right)


# 快排:空间复杂度nlog(n)
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [i for i in arr[1:] if i < pivot]
    right = [i for i in arr[1:] if i >= pivot]
    return quickSort(left) + pivot + quickSort(right)


def quickSort2(arr, left=None, right=None):
    if len(arr) <= 1:
        return arr
    def partition(arr, left, right):
        pivot = arr[left]
        while left < right:
            if left < right and arr[right] >= pivot:
                right -= 1
            arr[left] = arr[right]
            if left < right and arr[left] <= pivot:
                left += 1
            arr[right] = arr[left]
        arr[left] = pivot
        print(arr)
        return left
    if left < right:
        pivotIndex = partition(arr, left, right)
        print(pivotIndex)
        quickSort2(arr, left, pivotIndex - 1)
        quickSort2(arr, pivotIndex + 1, right)
    return arr


def buildMaxHeap(arr):
    for i in range(len(arr)//2)[::-1]:
        heapify(arr, i)


def heapify(arr, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < arrLen and arr[left] > a[largest]:
        largest = left
    if right < arrLen and arr[right] > a[largest]:
        largest = right
    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(arrLen)[::-1]:
        swap(arr, 0, i)
        arrLen -= 1
        heapify(arr, 0)
    return arr


def countSort(arr):
    bucket = [0] * (max(arr) + 1)
    for num in arr:
        bucket[num] += 1
    i = 0
    for j in range(len(arr)):
        while bucket[j] > 0:
            arr[i] = j
            bucket[j] -= 1
            i += 1
    return arr


if __name__ == '__main__':
    a = [4,5,6,7,3,2,6,9,8]
    # print(shellSort(a))
    print("quciksort")
    # print(quickSort2(a, 0, 8))
    # print(heapSort(a))
    print(a)
