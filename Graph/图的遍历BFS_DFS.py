#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 图的遍历BFS_DFS.py
# @Date  : 2019/4/2 0002
# @Contact : 1329778364@qq.com
# @Author: DeepMan
import Tree.utils as util


# 对图进行链式存储，列表中的每一个元素代表一个vertex 其包含value 和邻居节点的列表


class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.read = False  # 标记是否被读取 ,防止二次读取


class Graph():
    def __init__(self):
        self.vertexList = []

    def build_graph(self):
        for i in range(1, 10):
            self.vertexList.append(Vertex(i))
        self.vertexList[3].neighbors = [self.vertexList[i]
                                        for i in range(4, 6)]
        self.vertexList[2].neighbors = [self.vertexList[i]
                                        for i in range(7, 8)]
        self.vertexList[1].neighbors = [self.vertexList[i]
                                        for i in range(2, 5)]
        self.vertexList[0].neighbors = [self.vertexList[i]
                                        for i in range(6, 9)]
        self.vertexList[4].neighbors = [self.vertexList[0]]

    def BFS(self, i):
        vertexnode = self.vertexList[i]  # 表示我们以哪个节点代表开始
        queue = util.queue()
        queue.append(vertexnode)
        while not queue.empty():
            cur = queue.pop()
            print(cur.value, "->", end="")
            cur.read = True
            for next in cur.neighbors:
                if not next.read:
                    next.read = True
                    queue.append(next)

    def DFS(self, i):
        vertex = self.vertexList[i]
        stack = util.stack()
        stack.push(vertex)
        while stack.length > 0:
            cur = stack.pop()
            print(cur.value, "->", end="")
            for next in cur.neighbors:
                if not next.read:
                    stack.push(next)

    def DFS1(self, vertex):  # 递归深度优先遍历
        if vertex is None:
            return
        print(vertex.value, "->", end="")
        vertex.read = True
        for next in vertex.neighbors:
            if not next.read:
                self.DFS1(next)


if __name__ == '__main__':

    """ *******************************************************************
    # 1 图的广度优先遍历
        # 1.利用队列实现
        # 2.从源节点开始依次按照宽度进队列，然后弹出
        # 3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
        # 4.直到队列变空
    """
    g = Graph()
    g.build_graph()
    # g.BFS(3)
    # 实例输出： 4 ->5 ->6 ->1 ->7 ->8 ->9 ->

    """ ********************************************************************
    # 2 图的深度优先遍历(非递归)
        # 1.利用栈实现
        # 2.从源节点开始把节点按照深度放入栈，然后弹出
        # 3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
        # 4.直到栈变空
    """
    # g.DFS(3)
    # 实例输出： 4 ->6 ->5 ->1 ->9 ->8 ->7 ->

    """
    2.1 递归实现
    4 ->5 ->1 ->7 ->8 ->9 ->6 ->
    """
    g.DFS1(g.vertexList[3])
