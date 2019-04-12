#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Dijkstra.py
# @Date  : 2019/4/6 0006
# @Contact : 1329778364@qq.com
# @Author: DeepMan
"""
单源最短路径问题
"""
from Graph.Adjacency_matrix_list import Graph, AdjNode

class newGraph(Graph):
    def __init__(self):
        self.num_v = 7
        self.num_e = 12
        super(newGraph, self).__init__()
        self.source_point = 1
        self.dist = [None for i in range(self.num_v + 1)]
        self.path = [None for i in range(self.num_v + 1)]
        self.collected = [False for i in range(self.num_v + 1)]  # 用于标记是否已经被访问过
        self.v1_v2 = [  # 分别表示v1 v2 weight
            [
                1, 2, 2], [
                1, 4, 1], [
                2, 4, 3], [
                2, 5, 10], [
                4, 5, 2], [
                4, 3, 2], [
                3, 1, 4], [
                4, 6, 8], [
                4, 7, 4], [
                3, 6, 5], [
                7, 6, 1], [
                5, 7, 6]]

    def build_list_Graph(self):  # 建立单向的图

        for i in range(1, self.num_e + 1):
            v1, v2, weight = self.v1_v2[i - 1]
            # 由于是链式存储的 每一个节点 中包含了所有与其相连的vertex
            # NewNode = AdjNode(adjv=v1,
            #                   next=self.adjList[v2].next,
            #                   weight=weight)  # 中接
            # self.adjList[v2].next = NewNode  # 反向的箭头
            NewNode = AdjNode(adjv=v2,
                              weight=weight,
                              next=self.adjList[v1].next)  # 将原来的next挂载新建立连接之后
            self.adjList[v1].next = NewNode  # 正向箭头

    # 初始化我们的距离和路径矩阵
    def init_dist_path(self):
        self.inf = float("inf") + 1
        for i in range(self.num_v + 1):
            self.dist[i] = self.inf
            self.path[i] = -1
        # 初始化源节点的dist为0和其相邻的节点的dist 为weight
        self.dist[self.source_point] = 0
        temp = self.adjList[self.source_point]
        while temp.next is not None:
            self.dist[temp.next.adjv] = temp.next.weight
            self.path[temp.next.adjv] = self.source_point
            temp = temp.next

        print("dist ", ng.dist[1:8])
        print("path ", ng.path[1:8])

    def findmin(self, s):
        min = 0  # 表示最小值的下标 此时为inf
        for i in range(1, self.num_v + 1):
            if (i !=
                    s) and (self.dist[i] < self.dist[min]) and not self.collected[i]:
                min = i
        return min

    def Dijkstra(self, s):

        while True:
            # 在dist中找到最小的dist 没有collected过的
            v = self.findmin(s)
            if v == self.source_point:
                break
            self.collected[v] = True
            temp = self.adjList[v]
            if temp is None:  # 这就避免可最后一个元素6
                return
            while temp.next is not None:
                w = temp.next.adjv
                if self.collected[w] == False:
                    if self.dist[v] + temp.next.weight < self.dist[w]:
                        self.dist[w] = self.dist[v] + temp.next.weight
                        self.path[w] = v
                temp = temp.next


if __name__ == '__main__':

    """
    用于测试Dijkstra算法-*****************************************
    """
    ng = newGraph()
    ng.build_list_Graph()
    ng.print_list_graph()
    ng.init_dist_path()
    ng.Dijkstra(ng.source_point)
    print("*" * 50)
    print("dist ", ng.dist[1:8])
    print("path ", ng.path[1:8])
