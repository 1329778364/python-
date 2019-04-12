#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Adjacency_matrix_list.py
# @Date  : 2019/4/1 0001
# @Contact : 1329778364@qq.com
# @Author: DeepMan

# 1 我们首先使用邻接矩阵来实现图
import numpy as np
from Tree import utils


class edge:  # 边
    def __init__(self, v1=0, v2=0, weight=None):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class AdjNode:  # 链表存储基本结构
    def __init__(self, weight=None, adjv=None, next=None):
        self.adjv = adjv  # 表示顶点的标号
        self.weight = weight
        self.next = next
        self.read = False


class Graph:
    def __init__(self):
        # self.inputparse() # 输入参数  调用的时候 将其还原
        self.graph_weigh = np.zeros((self.num_v, self.num_v))  # 初始化权重为0 这是用于邻接矩阵定义的
        self.adjList = [
            None for _ in range(
                self.num_v+1)]  # 在这里调用 方便其他函数进行调用
        for i in range(1, self.num_v + 1):  # 邻接表进行初始化
            self.adjList[i] = AdjNode(adjv=i, weight=None, next=None)

    def inputparse(self):
        try:
            self.num_v = int(input("请输入图中包含的顶点数："))
            self.num_e = int(input("请输入边数："))
        except BaseException:
            print("请按要求输入，谢谢！")

    def insert_edge(self, edge):
        # 有向图 插入边 <V1,V2>
        self.graph_weigh[edge.v1][edge.v2] = edge.weight
        #  如果是无向图，还需要插入边 <V2,V1>
        self.graph_weigh[edge.v2][edge.v1] = edge.weight

    def build_graph(self):
        if self.num_e != 0:
            E = edge()
            for i in range(self.num_e):
                E.v1, E.v2, E.weight = map(
                    int, input("请输入两个顶点和其对应的边weight（以空格区分）：").split(' '))
                self.insert_edge(E)

    def orderTravel(self):
        for i in range(self.num_v):
            for j in range(self.num_v):
                print("%d" % (self.graph_weigh[i][j]), end=" ")
            print()

    # 利用邻接表建图
    def build_list_Graph(self):

        for i in range(self.num_e):
            v1, v2, weight = map(
                int, input("请输入两个顶点v1 v2 和其对应的边weight（以空格区分）：").split(' '))

            # 由于是链式存储的 每一个节点 中包含了所有与其相连的vertex
            NewNode = AdjNode(adjv=v1,
                              next=self.adjList[v2].next,
                              weight=weight)  # 中接
            self.adjList[v2].next = NewNode  # 反向的箭头

            NewNode = AdjNode(adjv=v2,
                              weight=weight,
                              next=self.adjList[v1].next)  # 将原来的next挂载新建立连接之后
            self.adjList[v1].next = NewNode  # 正向箭头

    def print_list_graph(self):  # 这里的遍历仅仅只是 直接与该节点进行相邻的节点 而BFS 相当于是遍历连通集

        for i in range(1, self.num_v + 1):
            temp = self.adjList[i]
            while temp:
                print("%d -> " % temp.adjv, end="")
                temp = temp.next
            print()

    # 广度优先搜索  （层序遍历）
    def BFS(self, AdjNode):  # 使用队列
        queue = utils.queue()
        queue.append(AdjNode)
        while not queue.empty():
            cur = queue.pop()
            print(cur.adjv, "-> ", end="")
            cur.read = True
            while cur.next is not None:
                temp = self.adjList[cur.next.adjv]
                if not temp.read:  # 关键在这里如果是读取过的 再次读取就会造成
                    queue.append(temp)
                cur = cur.next


if __name__ == '__main__':
    """
    1. 利用邻接矩阵进行表示：**************************************
    示例输入：
        请输入图中包含的顶点数：5
        请输入边数：3
        请输入两个顶点和其对应的边weight（以空格区分）：1 2 10
        请输入两个顶点和其对应的边weight（以空格区分）：2 3 20
        请输入两个顶点和其对应的边weight（以空格区分）：3 4 30
        输出的邻接矩阵：
        0  0  0   0  0
        0  0  10  0  0
        0  10 0   20 0
        0  0  20  0  30
        0  0  0   30 0
    """
    # g = Graph()
    # g.build_graph()
    # g.orderTravel()

    """
    2. 利用邻接表表示：************************************************************
    实际就是利用链表来存储数据，每一个顶点创建一个链表表示它所有直接相连的邻居

    特点：
        方便找任一顶点的所有邻接顶点
        节省稀疏图的空间
            需要 N 个头指针 + 2E 个结点（每个结点至少 2 个域）
        对于是否方便计算任一顶点的度
            无向图：方便
            有向图：只能计算出度
        不方便检查任意一对顶点间是否存在边
    """
    g1 = Graph()
    g1.build_list_Graph()
    g1.print_list_graph()
    g1.BFS(g1.adjList[3])

    """
    例子：
        请输入图中包含的顶点数：5
        请输入边数：3
        请输入两个顶点v1 v2 和其对应的边weight（以空格区分）：1 2 10
        请输入两个顶点v1 v2 和其对应的边weight（以空格区分）：2 3 20
        请输入两个顶点v1 v2 和其对应的边weight（以空格区分）：3 4 30
        输出：
        0 ->
        1 -> 2 ->
        2 -> 3 -> 1 ->
        3 -> 4 -> 2 ->
        4 -> 3 ->
    """
    # g1.BFS(g1.adjList[3])
