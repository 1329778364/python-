#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Floyd.py
# @Date  : 2019/4/7 0007
# @Contact : 1329778364@qq.com
# @Author: DeepMan

from Graph.Adjacency_matrix_list import Graph, AdjNode, edge
from Graph.Dijkstra import newGraph
import numpy as np
from Tree.utils import stack


class FloydGraph(newGraph):  # 建立Floyd图
    def __init__(self):
        super(FloydGraph, self).__init__()
        self.graph_weigh = np.zeros(
            (self.num_v + 1, self.num_v + 1))  # 初始化权重为0 这是用于邻接矩阵定义的

        for i in range(1, self.num_v + 1):
            for j in range(1, self.num_v + 1):
                if i == j:
                    self.graph_weigh[i][j] = 0
                else:
                    self.graph_weigh[i][j] = np.inf  # 将权重矩阵初始化为inf
        self.build_graph()  # 得到真实的权重矩阵
        self.D = self.graph_weigh.copy()
        self.path_folyd = np.zeros((self.num_v + 1, self.num_v + 1))

    def insert_edge(self, edge):
        # 有向图 插入边 <V1,V2>
        self.graph_weigh[edge.v1][edge.v2] = edge.weight
        #  如果是无向图，还需要插入边 <V2,V1>
        self.graph_weigh[edge.v2][edge.v1] = edge.weight

    def build_graph(self):
        if self.num_e != 0:
            E = edge()
            for i in range(self.num_e):
                E.v1, E.v2, E.weight = self.v1_v2[i]
                self.insert_edge(E)

    def Floyd(self):
        for i in range(1, self.num_v + 1):
            for j in range(1, self.num_v + 1):
                self.D[i][j] = self.graph_weigh[i][j]
                self.path_folyd[i][j] = -1
        for k in range(1, self.num_v + 1):
            for i in range(1, self.num_v + 1):
                for j in range(1, self.num_v + 1):
                    if (self.D[i][k] + self.D[k][j]) < self.D[i][j]:
                        self.D[i][j] = self.D[i][k] + self.D[k][j]
                        self.path_folyd[i][j] = k

    def print_path_ij(self, src, des):  # 借助递归的思想 我们用堆栈来实现
        s = stack()
        s.push(des)
        k = self.path_folyd[src][des]
        while k != -1:
            s.push(int(k))
            pp = int(k)
            k = self.path_folyd[src][pp]
        s.push(int(src))

        while not s.empty():
            print(s.pop(), "->", end="")


if __name__ == '__main__':
    """
    [[ 0.  0.  0.  0.  0.  0.  0.  0.]
     [ 0. -1. -1.  4. -1.  4.  7.  4.]
     [ 0. -1. -1.  4. -1.  4.  7.  4.]
     [ 0.  4.  4. -1. -1.  4. -1.  4.]
     [ 0. -1. -1. -1. -1. -1.  7. -1.]
     [ 0.  4.  4.  4. -1. -1.  7. -1.]
     [ 0.  7.  7. -1.  7.  7. -1. -1.]
     [ 0.  4.  4.  4. -1. -1. -1. -1.]]

    1 ->6 : 1  4  7  6
    """
    f = FloydGraph()
    f.Floyd()
    print(f.graph_weigh)  # 邻接矩阵 有直接相连的有值 否则为inf 然后通过Floyd 算法找到间接路径的最小值 即得到D
    print(f.path_folyd)  # 表示i到j 经过的节点k 最接近j的节点 因此我们可以通过递归的方法得到i到j上的所有点
    print(f.D)  # 是任意两点之间的距离

    print("*" * 50)
    f.print_path_ij(1, 6)  # 我们要查询两个点之间的最短路径

