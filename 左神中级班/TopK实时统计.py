import random
from typing import List, Dict, Optional

"""
设计并实现TopKRecord结构，可以不断地向其中加入字符串，并且可以根据字
符串出现的情况随时打印加入次数最多的前k个字符串。具体为:
1）k在TopKRecord实例生成时指定，并且不再变化(k是构造TopKRecord的参数)。
2）含有 add(String str)方法，即向TopKRecord中加入字符串。
3）含有 printTopK()方法，即打印加入次数最多的前k个字符串，打印有哪些
字符串和对应的次数即可，不要求严格按排名顺序打印。
4）如果在出现次数最多的前k个字符串中，最后一名的字符串有多个，比如出
现次数最多的前3个字符串具体排名为：
A 100次 B 90次 C 80次 D 80次 E 80次，其他任何字符串出现次数都
不超过80次
那么只需要打印3个，打印ABC、ABD、ABE都可以。也就是说可以随意抛弃最
后一名，只要求打印k个
要求：
1）在任何时候，add 方法的时间复杂度不超过 O(logk)
2）在任何时候，printTopK方法的时间复杂度不超过O(k)。
"""

class Node:
    """字符串节点，包含字符串和出现次数"""
    def __init__(self, s: str, t: int):
        self.str = s
        self.times = t

class TopKRecord:
    """实时TopK记录器，使用最小堆实现"""
    def __init__(self, size):
        self.heap = [None] * size
        self.index = 0
        self.str_node_map = dict()
        self.node_index_map = dict()
        self.size = size

    def swap(self, idx1, idx2):
        self.node_index_map[self.heap[idx1]] = idx2
        self.node_index_map[self.heap[idx2]] = idx1

        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def print_top_k(self):
        for i in range(self.size):
            if i >= self.index or self.heap[i] is None:
                break
            print(f"Str: {self.heap[i].str}")
            print(f"Times: {self.heap[i].times}")


    def heap_insert(self, idx):
        while idx != 0:
            parent = (idx - 1) // 2
            if self.heap[idx]. times < self.heap[parent].times:
                self.swap(parent, idx)
                idx = parent
            else:
                break

    def heapify(self, index, heap_size):
        l = index * 2 + 1
        r = index * 2 + 2
        smallest = index
        while l < heap_size:
            if self.heap[l].times < self.heap[index].times:
                smallest = l
            if r < heap_size and self.heap[r].times < self.heap[smallest].times:
                smallest = r
            if index != smallest:
                self.swap(index, smallest)
            else:
                break
            index = smallest
            l = index * 2 + 1
            r = index * 2 + 2

    def add(self, s):
        """添加字符串，更新频率统计"""
        cur_node = None
        pre_index = -1
        
        if s not in self.str_node_map:
            # 新字符串
            cur_node = Node(s, 1)
            self.str_node_map[s] = cur_node
            self.node_index_map[cur_node] = -1
        else:
            # 已存在字符串，增加计数
            cur_node = self.str_node_map[s]
            cur_node.times += 1
            pre_index = self.node_index_map.get(cur_node, -1)
        
        if pre_index == -1:
            # 字符串不在堆中
            if self.index == self.size:
                # 堆已满，检查是否需要替换
                if self.heap[0].times < cur_node.times:
                    # 移除堆顶元素的映射
                    self.node_index_map[self.heap[0]] = -1
                    # 将新节点放入堆顶
                    self.node_index_map[cur_node] = 0
                    self.heap[0] = cur_node
                    # 调整堆
                    self.heapify(0, self.index)
            else:
                # 堆未满，直接添加
                self.node_index_map[cur_node] = self.index
                self.heap[self.index] = cur_node
                self.heap_insert(self.index)
                self.index += 1
        else:
            # 字符串已在堆中，调整堆
            self.heapify(pre_index, self.index)


