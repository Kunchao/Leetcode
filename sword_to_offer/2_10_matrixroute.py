#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25
# @Author  : Vapor
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(matrix) == 0 or rows < 1 or cols < 1 or len(path) == 0:
            return False
        x = [list(matrix[i*cols: i*cols+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.isHashPath(x, i, j, path):
                    return True
        return False

    def isHashPath(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            print(matrix[i][j])
            if not p[1:]:
                return True
            # 暂时修改maxtrix的标识，相当于true和false标志
            matrix[i][j] = ''
            if i < len(matrix) - 1 and self.isHashPath(matrix, i+1, j, p[1:]):
                return True
            elif i >= 1 and self.isHashPath(matrix, i-1, j, p[1:]):
                return True
            elif j < len(matrix[0]) - 1 and self.isHashPath(matrix, i, j+1, p[1:]):
                return True
            elif j >= 1 and self.isHashPath(matrix, i, j-1, p[1:]):
                return True
            matrix[i][j] = p[0]
            return False
        else:
            return False


if __name__ == '__main__':
    print(Solution().hasPath("ABCESFCSADEE", 3, 4, "ABCCED"))
