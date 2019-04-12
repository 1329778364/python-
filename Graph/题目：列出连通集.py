#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 题目：列出连通集.py
# @Date  : 2019/4/2 0002
# @Contact : 1329778364@qq.com
# @Author: DeepMan

import Graph.Adjacency_matrix_list as graph


class newGraph(graph.Graph):  # 创建一个新图
    def __init__(self):
        super(newGraph, self).__init__()
        self.readVertex_DFS = [None for _ in range(self.num_v)]
        self.readVertex_BFS = [None for _ in range(self.num_v)]
        self.build_graph()

    def DFS(self, v):
        self.readVertex_DFS[v] = True
        print(v, "->", end="")
        for i in range(self.num_v):
            if (not self.readVertex_DFS[i] and self.graph_weigh[v][i]):
                self.DFS(i)

    def BFS(self, v):
        queue = graph.utils.queue()
        queue.append(v)

        while not queue.empty():
            temp = queue.pop()
            print(temp, "->", end="")
            self.readVertex_BFS[temp] = True
            for i in range(self.num_v):
                if self.graph_weigh[temp][i] and not self.readVertex_BFS[i]:
                    queue.append(i)

    def travel_component(self):  # 遍历图中所有的连通集
        for i in range(self.num_v):
            if not self.readVertex_BFS[i]:
                self.BFS(i)
                print()

        print("****" * 20)

        for i in range(self.num_v):
            if not self.readVertex_DFS[i]:
                self.DFS(i)
                print()


ng = newGraph()
ng.travel_component()
