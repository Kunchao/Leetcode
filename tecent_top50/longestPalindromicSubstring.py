#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18
# @Author  : Vapor


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         resverse = s[::-1]
#         maxLen = 0
#         maxEnd = 0
#         n = len(s)
#         a = [[0 for i in range(n)] for i in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 if s[i] == resverse[j]:
#                     if i == 0 or j == 0:
#                         print(s[i], resverse[j], s[i] == resverse[j], i, j)
#                         a[i][j] = 1
#                     else:
#                         a[i][j] = a[i-1][j-1] + 1
#
#                 if maxLen <= a[i][j]:
#                     beforeRec = n - j - 1
#                     if beforeRec + a[i][j] - 1 == i:
#                         maxLen = a[i][j]
#                         maxEnd = i
#                         print(i, j, maxLen)
#         for i in a:
#             print(i)
#         return s[maxEnd - maxLen + 1: maxLen+1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1: return ""
        n = len(s)
        start = end = 0
        for i in range(n):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            print(len1, "greater or less", len2)
            maxLen = max(len1, len2)
            if maxLen > end - start:
                start = i - (maxLen-1) // 2
                end = i + maxLen // 2
        print(i, maxLen, start, "=", end)
        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        l = left
        r = right
        while (r<len(s) and l>=0) and s[l] == s[r]:
            print(l, r)
            l -= 1
            r += 1
            print(l, r)
        return r-l-1



if __name__ == '__main__':
    # s = 'cbbd'
    # s = 'babad'
    s = 'ac'
    print(Solution().longestPalindrome(s))