#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Prim.py
# @Date  : 2019/4/9 0009
# @Contact : 1329778364@qq.com
# @Author: DeepMan

from Graph.Adjacency_matrix_list import Graph, edge
import numpy as np


class newGraph(Graph):
    def __init__(self):
        self.num_v = 7
        self.num_e = 12
        super(newGraph, self).__init__()
        self.v1_v2 = [  # 分别表示v1 v2 weight
            [1, 2, 2],
            [1, 4, 1],
            [1, 3, 4],
            [2, 4, 3],
            [2, 5, 10],
            [3, 4, 2],
            [3, 6, 5],
            [4, 5, 7],
            [4, 6, 8],
            [4, 7, 4],
            [7, 6, 1],
            [5, 7, 6]]
        self.graph_weigh = np.zeros(
            (self.num_v + 1, self.num_v + 1))  # 初始化权重为0 这是用于邻接矩阵定义的
        self.dist = [np.inf for _ in range(self.num_v + 1)]  # 初始化距离
        self.parent = [-1 for _ in range(self.num_v + 1)]  # 初始化并查集
        self.MST = []
        self.sum = 0

    # 建图
    def build_graph(self):
        if self.num_e != 0:
            for i in range(self.num_e):
                self.graph_weigh[self.v1_v2[i][0]][self.v1_v2[i][1]] = self.v1_v2[i][2]
                self.graph_weigh[self.v1_v2[i][1]][self.v1_v2[i][0]] = self.v1_v2[i][2]

    # Prim算法前的初始化  假设以1号节点为开始
    # 首先找到他的所有邻居节点的weight 并使他们的父节点为1号节点
    def InitPrim(self, s):
        self.dist[s] = 0
        self.MST.append(s)
        for i in range(1, self.num_v + 1):
            if self.graph_weigh[s][i]:
                self.dist[i] = self.graph_weigh[s][i]
                self.parent[i] = s
        print(self.dist)

    # 查找未收录中dist最小的点
    def FindMin(self):
        min = np.inf
        xb = -1
        for i in range(1, self.num_v + 1):  # 未收录顶点中dist最小者
            if(self.dist[i] !=0 and self.dist[i] < min): # 不等于零表示没有收录
                min = self.dist[i]
                xb = i # 记录最小值的下标 如果全都访问过了 则返回-1
        return xb

    def Prim(self, s):
        self.InitPrim(s)  # 记录最小生成树的开始节点
        while True:
            v = self.FindMin()  # 未收录顶点中dist最小者
            if v == -1:
                break
            self.sum += self.dist[v] # 将路径长度进行加和
            self.dist[v] = 0 # 表示已经将节点计入生成树中
            self.MST.append(v)
            for w in range(1, self.num_v + 1):  # 查找V的邻居节点，并且邻居节点没有被访问 即dist[w] != 0
                if self.graph_weigh[v][w] and self.dist[w]:
                    if self.graph_weigh[v][w] < self.dist[w]: # 判断是否需要更新weight的值
                        self.dist[w] = self.graph_weigh[v][w] # 记录上一轮的最近距离节点与w节点的距离
                        self.parent[w] = v

    def output(self):
        print("被收录的顺序：", end="")
        for i in range(self.num_v):
            print(self.MST[i], "->", end="")
        print()
        print("权重之和为：%d ->" % self.sum)

        print("节点的parent节点为：", end="")
        for i in range(1, self.num_v + 1):
            print(self.parent[i], "->", end="")

    def printweight(self):
        print(self.graph_weigh[1:])

if __name__ == '__main__':

    """
    被收录的顺序：1 ->4 ->2 ->3 ->7 ->6 ->5 ->
    权重之和为：16 ->
    节点的parent节点为：-1 ->1 ->4 ->1 ->7 ->7 ->4 ->
    """
    g = newGraph()
    g.build_graph()
    g.printweight()
    g.Prim(1)
    g.output()

