#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 哈夫曼编码.py
# @Date  : 2019/3/30 0030
# @Contact : 1329778364@qq.com
# @Author: DeepMan


from Tree.p64_path_of_stack import minHeap
"""
对于不同频率出现的字符怎么编码效率高
举个例子成绩的判断：将高频率的成绩判断放在前面
查找效率 = 概率 * 判别次数

目标就是根据不同的查找效率构造更加有效的搜索树

哈夫曼树的构造:
首先，将所有节点按权值大小进行排列
每次把权值最小的两颗二叉树合并 （可以使用最小堆来实现）

"""
"""
4. 最小堆实现哈夫曼树

堆里本来就是放东西的，既然可以放数…那为什么不能放树，醍醐灌顶
"""

MaxSize = 1000
MinData = -1000
A = [1, 3, 5, 8]  # 预先定义好一组权值
A_length = 4


class HuffmanTree:
    def __init__(self, weight=0, left=None, right=None):
        self.weight = weight
        self.left = left
        self.right = right


# 创建一个包含huffmantree 的heap 类
class huffmanHeap(minHeap):  # 当然我们使用的是最小堆来实现
    def __init__(self):
        super(huffmanHeap, self).__init__(size=0, maxsize=MaxSize)
        huff = HuffmanTree(weight=MinData)
        self.heap_arr[0] = huff  # 存放哈夫曼树的堆
        print(self.heap_arr)

    # 调整子最小堆

    def sort(self, i):
        temp = self.heap_arr[int(i)].weight  # 取出当前"根结点"值
        paretn = i
        while 2 * paretn <= self.size:
            child = 2 * paretn
            if (child != self.size) and (
                    self.heap_arr[int(child) + 1].weight < self.heap_arr[int(child)].weight):
                child += 1
            if self.heap_arr[int(child)].weight >= temp:
                break
            else:
                self.heap_arr[paretn] = self.heap_arr[child]
            paretn = child
        self.heap_arr[int(paretn)].weight = temp

    # 调整最小堆
    def adjust(self):
        i = self.size / 2
        while i > 0:
            self.sort(i)
            i -= 1

    # 建堆
    def buildhuffheap(self):
        i = 0
        while i < A_length:
            huff = HuffmanTree(weight=A[i])
            self.size += 1
            self.heap_arr[self.size] = huff
            i += 1
        self.adjust()

    def delet(self):
        t = self.heap_arr[1]
        temp = self.heap_arr[self.size]
        self.size -= 1
        paretn = 1
        while paretn * 2 < self.size:
            child = 2 * paretn
            if (child != self.size) and (
                    self.heap_arr[child + 1].weight < self.heap_arr[child].weight):
                child += 1
            if self.heap_arr[child].weight >= temp.weight:
                break
            else:
                self.heap_arr[paretn] = self.heap_arr[child]
            paretn = child
        self.heap_arr[paretn] = temp
        return t

    def Insert(self, huffmanTree):
        weight = huffmanTree.weight
        self.size += 1
        i = self.size
        while self.heap_arr[int(i / 2)].weight > weight:
            self.heap_arr[int(i)] = self.heap_arr[int(i / 2)]
            i /= 2
        self.heap_arr[int(i)] = huffmanTree

    def preOrderTraversal(self, huffmanTree):
        if(huffmanTree):
            print(huffmanTree.weight)
            self.preOrderTraversal(huffmanTree.left)
            self.preOrderTraversal(huffmanTree.right)

    def Huffman(self):
        self.buildhuffheap()
        times = self.size
        i = 1
        while i < times:
            T = HuffmanTree()
            T.left = self.delet()
            T.right = self.delet()
            T.weight = T.left.weight + T.right.weight
            self.Insert(T)
            i += 1
        T = self.delet()
        return T


if __name__ == '__main__':
    H = huffmanHeap()
    huff = H.Huffman()
    H.preOrderTraversal(huff)
