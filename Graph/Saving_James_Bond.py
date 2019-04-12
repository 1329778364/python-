#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Saving_James_Bond.py
# @Date  : 2019/4/4 0004
# @Contact : 1329778364@qq.com
# @Author: DeepMan
import numpy as np
from math import *

# 这是一种比较复杂的方法，当然还有其他更加有效的方法


class crocodile:
    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.visited = False
        self.jump = False  # 表示该条鳄鱼能否上岸


class newGraph:
    def __init__(self):
        self.crocodile_num = 10
        self.crocodileList = []
        self.distance = 20  # 表示多大的范围能够进行跳跃  即构建连接矩阵的判据
        self.graph_weigh = np.zeros(
            (self.crocodile_num, self.crocodile_num))  # 初始化权重为0
        self.one_step_jump = []
        self.could_final_jump = False

    def build_graph(self):
        # 初始化所有节点
        for i in range(self.crocodile_num):
            x = np.random.randint(low=-50, high=50, size=2)[0]
            y = np.random.randint(low=-50, high=50, size=2)[1]
            self.crocodileList.append(crocodile(x_axis=x, y_axis=y))
        # 构建邻接矩阵 双向图
        for i in range(self.crocodile_num):
            if (50 - abs(self.crocodileList[i].x_axis) < self.distance) or (50 -
                                                                            abs(self.crocodileList[i].y_axis) < self.distance):
                self.crocodileList[i].jump = True

            for j in range(i, self.crocodile_num):
                distance = self.caculate_distance(
                    self.crocodileList[i], self.crocodileList[j])
                if distance < self.distance:
                    self.graph_weigh[i][j] = distance
                    self.graph_weigh[j][i] = distance

    def DFS(self, v):
        self.crocodileList[v].visited = True
        print(v, "->", end="")
        for i in range(self.crocodile_num):
            if (not self.crocodileList[i].visited and self.graph_weigh[v][i]):
                self.DFS(i)
                if self.crocodileList[i].jump:
                    self.could_final_jump = True


    def travel_component(self):  # 遍历图中能够在一跳范围内 的连通集
        for i in self.one_step_jump:
            if not self.crocodileList[i].visited:
                self.DFS(i)
                print()

    def find_neghbors(self):  # 找到james 可以跳的节点
        james = crocodile(0, 0)
        for i in range(self.crocodile_num):
            distance = self.caculate_distance(james, self.crocodileList[i])
            if distance < self.distance:
                self.one_step_jump.append(i)

    def caculate_distance(self, cro1, cro2):  # 计算两只鳄鱼之间的距离
        distance = sqrt((cro1.x_axis - cro2.x_axis)**2 +
                        (cro1.y_axis - cro2.y_axis)**2)
        if distance <= self.distance:
            return distance
        else:
            return 0

    def orderTravel(self):
        for i in range(self.crocodile_num):
            for j in range(self.crocodile_num):
                print("%d" % (self.graph_weigh[i][j]), end=" ")
            print()


ng = newGraph()
ng.build_graph()
ng.find_neghbors()
ng.travel_component()
print(ng.could_final_jump)
