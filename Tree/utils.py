#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : utils.py
# @Date  : 2019/3/28 0028
# @Contact : 1329778364@qq.com
# @Author: DeepMan

from collections import deque


class stack:
    def __init__(self):
        self.stack = deque()
        self.length = 0

    def push(self, value):
        self.stack.append(value)  # 使用队列的追加来实现
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.stack.pop()  # 将 最后的元素pop出来


    def empty(self):
        return len(self.stack) == 0


class queue:
    def __init__(self):
        self.queue = deque()

    def append(self, value):
        self.queue.append(value)  # 使用队列的追加来实现

    def pop(self):
        return self.queue.popleft()  # 将 最后的元素pop出来

    def empty(self):
        return len(self.queue) == 0


class BinaryTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.heigh = 0

    # 构建一棵树  由于递归调用需要两个参数  所以 我们可以定义连个方法  来分别对左右子树进行判定
    # 递归调用创建一棵树
    def insert(self, value, BST):
        if not BST:
            BST = BinaryTree(value)
        elif value < BST.data:  # 保证在左子树的值都小于根节点
            BST.left = self.insert(value, BST.left)
        elif value > BST.data:  # 保证在右子树的值都大于根节点
            BST.right = self.insert(value, BST.right)
        else:  # 如果相等则什么都不做
            pass
        return BST
