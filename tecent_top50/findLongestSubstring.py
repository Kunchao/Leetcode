#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/18
# @Author  : Vapor


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = j = 0
        words = set()
        ans = 0
        while i < n and j < n:
            if s[j] not in words:
                words.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                words.remove(s[i])
                i += 1
        return ans


if __name__ == '__main__':
    a = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(a))


