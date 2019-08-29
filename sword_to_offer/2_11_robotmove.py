#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25
# @Author  : Vapor
# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 | rows < 0 | cols < 0:
            return -1
        visit = [list([False for i in range(cols)]) for i in range(rows)]
        return self.helper(threshold, rows, cols, 0, 0, visit)

    def helper(self, threshold, rows, cols, i, j, visit):
        count = 0
        if i >= 0 and j >= 0 and i < rows and j < cols and \
            not visit[i][j] and self.getDigitSum(i) + self.getDigitSum(j) <= threshold:
            visit[i][j] = True
            count = 1 + self.helper(threshold, rows, cols, i-1, j, visit) + \
                        self.helper(threshold, rows, cols, i+1, j, visit) + \
                        self.helper(threshold, rows, cols, i, j+1, visit) + \
                        self.helper(threshold, rows, cols, i, j-1, visit)
        return count

    def getDigitSum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10
            number = number // 10
        return sum


if __name__ == '__main__':
    print(Solution().movingCount(5, 10, 10))
    # print(Solution().getDigitSum(-1))



