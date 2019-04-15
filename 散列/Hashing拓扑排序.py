#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Hashing拓扑排序.py
# @Date  : 2019/4/15 0015
# @Contact : 1329778364@qq.com
# @Author: DeepMan


"""
使用hash函数和拓扑排序中的知识
"""
import numpy as np
from Tree import queue


class Graph:
    def __init__(self):
        self.value = [33, 1, 13, 12, 34, 38, 27, 22, 32, -1, 21]
        self.N = len(self.value)
        self.index_map_value = {}
        self.weigh = np.zeros((self.N, self.N))
        for i in range(self.N):
            for j in range(self.N):
                self.weigh[i][j] = np.inf
        self.indegree = [None for _ in range(11)]
        self.stack = queue()

    def Insert(self):
        for i in range(self.N):
            if 0 <= self.value[i]:
                self.index_map_value[self.value[i]] = i
                remainder = self.value[i] % self.N
                if remainder == i:
                    self.indegree[i] = 0  # 表示为没有发生冲突的数
                else:
                    self.indegree[i] = (i - remainder + self.N) if\
                        (i - remainder < 0) else (i - remainder)
                    j = remainder
                    while j != i:
                        self.weigh[i][j] = 1
                        j = (j + 1) % self.N

    def TopSort(self):
        for i in range(self.N):
            if (self.indegree[i] !=None and 0 < self.value[i]):
                self.stack.append(self.value[i])
        flag = True
        while not self.stack.empty():
            tempval = self.stack.pop()
            index = self.index_map_value[tempval]
            if flag:
                flag = False
            else:
                print(" ", end="")
            print(tempval, end="")
            for i in range(self.N):
                if self.weigh[index][i] != np.inf:
                    if --self.indegree[i] == 0:
                        self.stack.append(self.value[i])


if __name__ == '__main__':

    # 首先根据原有的建立拓扑图
    g = Graph()
    g.Insert()
    print(g.weigh)
    print(g.indegree)
    g.TopSort()
