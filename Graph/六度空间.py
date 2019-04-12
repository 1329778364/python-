#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 六度空间.py
# @Date  : 2019/4/5 0005
# @Contact : 1329778364@qq.com
# @Author: DeepMan
from queue import Queue
from Graph.Adjacency_matrix_list import AdjNode, Graph
import numpy as np


class GraphList(Graph):
    def __init__(self):
        self.inputparse()
        super(GraphList, self).__init__()
        self.min_max = (5, 10)

    def inputparse(self):
        try:
            self.num_v = int(input("请输入图中包含的顶点数："))
        except BaseException:
            print("请按要求输入，谢谢！")

    def build_list_Graph(self):
        for i in range(1, self.num_v+1):
            count = 0
            # 每个人随机产生50-100之间的联系人
            m = np.random.randint(self.min_max[0], self.min_max[1])
            # 联系人从10000个人里面随机选出m位联系人
            l = list(range(1, self.num_v+1))
            np.random.shuffle(l)
            for v in l:
                if v != i:
                    count += 1

                if count == m:
                    break

    def print_list_graph(self):
        for i in range(self.num_v):
            temp = self.graph[i]
            print("%d ->" % i, end="")
            for i in range(len(temp)):
                print("%d->" % temp[i], end="")
            print()

    def SDS(self):
        self.print_list_graph()
        degree = self.BFS(0, self.graph)
        print(degree)
        # for i in range(self.num_v):
        #     degree = self.BFS(i, self.graph)
        #     print(degree)

    def BFS(self, start, graph):
        queue = Queue()
        queue.put([start, 0])
        vis = [False for _ in range(len(graph))]
        vis[start] = True
        maxDegree = 0
        while not queue.empty():
            node, degree = queue.get()
            maxDegree = degree
            for nextNode in graph[node]:
                if not vis[nextNode]:
                    queue.put([nextNode, degree + 1])
                    vis[nextNode] = True
        return maxDegree


gl = GraphList()
gl.build_list_Graph()
gl.SDS()
#
# 模拟一万个人空间的六度空间
# 每个人大概可以与50-100个人形成直接联系,因为会有重复，每个人实际上直接进入下一层的人数小于50-100人


# def BFS(start, graph):
#     queue = Queue()
#     queue.put([start, 0])
#     vis = [False for _ in range(len(graph))]
#     vis[start] = True
#     maxDegree = 0
#     while not queue.empty():
#         node, degree = queue.get()
#         maxDegree = degree
#         for nextNode in graph[node]:
#             if not vis[nextNode]:
#                 queue.put([nextNode, degree + 1])
#                 vis[nextNode] = True
#     return maxDegree
#
#
# n = 10000
# min_max = (5, 10)
# # 建立邻接表
# graph = [[] for _ in range(n)]
# for i in range(n):
#     # 每个人随机产生50-100之间的联系人
#     m = np.random.randint(min_max[0], min_max[1])
#     # 联系人从10000个人里面随机选出m位联系人
#     l = list(range(n))
#     np.random.shuffle(l)
#     for v in l:
#         if v != i:
#             graph[i].append(v)
#         if len(graph[i]) == m:
#             break
#
# print('Six Degrees of Separation')
# degree = BFS(0, graph)
# print('max degree is: %d' % degree)
