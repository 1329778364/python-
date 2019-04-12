#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 链表基础知识.py
# @Date  : 2019/3/24 0024
# @Contact : 1329778364@qq.com 
# @Author: DeepMan
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newdata):
        self.data = newdata

    def setNext(self, nextNode):
        self.next = nextNode


# 定义一个无序链表
class List():
    def __init__(self):
        # self.node = Node(10)/
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, value):
        newnode = Node(value)
        newnode.setNext(self.head)
        self.head = newnode # 更新 头节点指针指向新的节点

    def append(self, value): # 尾部增加节点， 首先 我们要到链表的尾部
        newnode = Node(value)
        current = self.head
        if self.isEmpty():
            self.head = newnode
        else:
            while current.getNext() is not None:
                # 这里有一个关键点，就是判断current是否是最后一个节点而不再是current是否为None ，
                # 因为最后一个节点的判断要素是其后没有节点， 也就是getNext()为None
                current = current.getNext()

            current.setNext(newnode)


    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, value): # 查找某个值 并返回其index
        current = self.head

        found = False
        p = None
        previous = None

        while current is not None and not found:

            if current.getData() == value:
                found = True
                p = current
            else:
                previous = current
                current = current.getNext()

        if previous == None:  # 当如果第一个就是要找的，那么就无法得到之前的节点.
            previous = self.head

        return found, p, previous


    def remove(self, value):
        current = self.head
        found, p, previous = self.search(value)
        # 我们先找到 再进行删除，同时要返回之前的节点。
        if not found:
            print("can't delet it, beacause of not find")
        else:
            previous.setNext(p.getNext())

    def insert(self, index, value): # 首先要找到对应的位置然后插入，如果是在表头index = 0 的情况下直接插入
        current = self.head
        newnode = Node(value)
        count = 0
        while current is not None:
            current = current.getNext()
            count += 1
            if count == index:
                newnode.setNext(current.getNext())
                current.setNext(newnode)
        if index == 0:
            self.head = newnode




myList = List()
myList.add(31)  # 这里的add 相当于是在链表的前面加 最后加入的反而在链表的head位置
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54)
myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54) # head


print(myList.size())

found = myList.search(17)
print(found)

myList.append(100) # tail
print(myList.size())
found = myList.search(100)
print(found)

myList.remove(54)
found = myList.search(54)
print(found)

print(myList.head)
myList.insert(10, 500)
found = myList.search(500)
print(found)
