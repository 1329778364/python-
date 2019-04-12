#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Kruskal.py
# @Date  : 2019/4/9 0009
# @Contact : 1329778364@qq.com
# @Author: DeepMan
from Graph.Prim import newGraph
import Tree.utils as u


class Node:  # 存储边的weight
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class KruskalGraph(newGraph):
    def __init__(self):
        super(KruskalGraph, self).__init__()
        self.s = u.stack()
        self.v1_v2 = [  # 分别表示v1 v2 weight
            [2, 5, 10],
            [4, 6, 8],
            [4, 5, 7],
            [5, 7, 6],
            [3, 6, 5],
            [1, 3, 4],
            [4, 7, 4],
            [2, 4, 3],
            [3, 4, 2],
            [1, 2, 2],
            [1, 4, 1],
            [7, 6, 1]]

    def build_graph(self):
        if self.num_e != 0:
            for i in range(len(self.v1_v2)):
                tempE = Node(
                    self.v1_v2[i][0],
                    self.v1_v2[i][1],
                    self.v1_v2[i][2])
                self.s.push(tempE)

    def Kruskal(self):
        # 最小生成树的边不到Nv-1 条并且还有边
        while (len(self.MST) != self.num_v - 1) and not self.s.empty():
            E = self.s.pop()  # 从最小堆取出一条权重最小的边 我们这里定义的就是最v1_v2就是最小堆
            # 检测两个节点是否在同一个集合
            if self.findparent(E.v1) != self.findparent(E.v2):  # 表明不在同一个集合
                self.sum += E.weight
                # 然后将这两个节点 联合到同一个集合当中
                # 或者  self.UnionVertex(E.x1, E.x2):
                self.anzhiguibing(E.v1, E.v2)
                self.MST.append(E)

    # 按规模归并
    def UnionVertex(self, x1, x2):
        # 找到两个节点的父节点 如果parent值为-1 那么久将返回他自己但是parent[x] 还是-1
        x1 = self.findparent(x1)
        x2 = self.findparent(x2)
        if self.parent[x1] < self.parent[x2]:  # x1的数的深度大于x2 将x2归并到x1 上面，同时x2的父节点设为x1
            self.parent[x1] += self.parent[x2]
            self.parent[x2] = x1
        else:
            self.parent[x2] += self.parent[x1]  # 将x1归并到x2上
            self.parent[x1] = x2               # 更新

    # 按秩归并
    def anzhiguibing(self, x1, x2):
        # 找到两个节点的父节点 如果parent值为-1 那么久将返回他自己但是parent[x] 还是-1
        x1 = self.findparent(x1)
        x2 = self.findparent(x2)
        if self.parent[x1] < self.parent[x2]:  # x1的数的深度大于x2 将x2归并到x1 上面，同时x2的父节点设为x1
            self.parent[x2] = x1
        else:
            if self.parent[x1] == self.parent[x2]:
                self.parent[x2] -= 1
            self.parent[x1] = x2  # 更新

    # 路径压缩查找
    def findparent(self, x):  # 找到一个节点的父亲节点 集合判断
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.findparent(self.parent[x])
            return self.parent[x]

    def output(self):
        print("被收入的顺序为：")
        print("  边  |weight   ")
        for i in range(len(self.MST)):
            print(self.MST[i].v1, "--", self.MST[i].v2, self.MST[i].weight)
        print("sum of weight:", self.sum)
        print("节点 |其父节点")
        for i in range(1, self.num_v + 1):
            print(i, "  ", self.parent[i])


if __name__ == '__main__':

    """按规模归并的结果：
    被收入的顺序为：
    边  |weight
    7 -- 6 1
    1 -- 4 1
    1 -- 2 2
    3 -- 4 2
    4 -- 7 4
    5 -- 7 6
    sum of weight: 16
    节点 |其父节点
    1    4
    2    4
    3    4
    4    -7
    5    4
    6    4
    7    4
    """
    kg = KruskalGraph()
    kg.build_graph()
    kg.Kruskal()
    kg.output()
    """
    # 按秩归并的结果：
    被收入的顺序为：
    边  |weight
    7 -- 6 1
    1 -- 4 1
    1 -- 2 2
    3 -- 4 2
    4 -- 7 4
    5 -- 7 6
    sum of weight: 16
    节点 |其父节点
    1    6
    2    4
    3    6
    4    6
    5    6
    6    -3
    7    6
    """
