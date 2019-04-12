#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 双向循环链表.py
# @Date  : 2019/3/24 0024
# @Contact : 1329778364@qq.com 
# @Author: DeepMan

class Node():

    __slots__ = ["prior", "data", "next"]

    def __init__(self, prior=None, data=None, next=None):
        self.prior = prior
        self.data = data
        self.next = next

class doubleCirclelist(object):

    def __init__(self, maxsize=None):
        node = Node()
        # 第一个节点 prior  与 next 都是指向自己本身的 node
        node.next, node.prior = node, node
        self.root = node # 一定要定义一个根节点 别忘了 用于指向 第一个节点
        self.maxsize = maxsize
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next  # 这里一定要注意root作为第一个节点  但不是头节点

    def tailnode(self):
        return self.root.prior

    def append(self, value):
        # when we append some ,1 判断是否还能够追加（达到maxsize） （判断是否满了）
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise ValueError("list is full, don't have size")

        # 然后进行追加 p -> prior  = o; o -> next = p ; p ->next = root; root.next = p

        newnode = Node(data=value)
        tailnode = self.tailnode() or self.root
        # 这里写root 是为了能够得到在第一次追加元素时在 root后面进行添加
        newnode.prior = tailnode
        tailnode.next = newnode

        newnode.next = self.root  # root始终是不会变得 所以每次追加的时候 其都指向root
        self.root.prior = newnode

        self.length += 1

    def appendLeft(self, value): # 注意 是在root后面议添加还是在前面添加 当然是后面拉，
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')

        newnode = Node(data=value)
        # 这里我们要注意是否是空节点 如果是空节点直接添加在root 后面
        if self.root.next == self.root:
            newnode.prior = self.root
            newnode.next = self.root
            self.root.next = newnode
            self.root.prior = newnode

        else: # 也是追加在root 后面 只不过原来与其相连的要进行断开
            headnode = self.root.next # 经过一个指向之后更容易理解 headnode其实就是root节点后面的第一个节点

            newnode.next = headnode
            headnode.prior = newnode

            self.root.next = newnode
            newnode.prior = self.root

        self.length += 1

    def iter_node(self):

        current = self.root.next

        if current == self.root:
            return
        while current.next is not self.root:  # current.next
            yield current
            current = current.next
        yield current

    def __iter__(self):
        for node in self.iter_node():
            yield node.data

    def inverse_iter(self):

        current = self.root.prior
        # 判断练链表是否为空
        if current == self.root:
            return

        while current.prior is not self.root:  # current.prior
            yield current
            current = current.prior
        yield current

    def remove(self, node): # 直接删除节点 不需要遍历查找到 （双端链表的优点）
        # 直接更改节点的两个地址便可
        # 这里输入的是节点  而不是value or index 所以比较方便

        if self.root == self.root.next:
            return

        # 进行删除操作 先与前面断开，然后与后面 断开
        node.prior.next = node.next
        node.next.prior = node.prior

        self.length -= 1
        return node


def test_example(maxsize=32):

    dll = doubleCirclelist(maxsize=maxsize)
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert list(dll) == [0, 1, 2]

    assert [node.data for node in dll.iter_node()] == [0, 1, 2]
    assert [node.data for node in dll.inverse_iter()] == [2, 1, 0]


    headnode = dll.headnode()
    assert headnode.data == 0
    dll.remove(headnode)
    assert len(dll) == 2
    assert [node.data for node in dll.iter_node()] == [1, 2]

    dll.appendLeft(0)
    assert [node.data for node in dll.iter_node()] == [0, 1, 2]


if __name__ == '__main__':
    test_example(32)









