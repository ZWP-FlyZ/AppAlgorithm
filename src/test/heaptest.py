# -*- coding: utf-8 -*-
'''
Created on 2018年9月7日

@author: zwp12
'''

import heapq;


class  node():
    val = 0;
    name='';
    def __init__(self,name,val):
        self.name=name;
        self.val=val;
    def __gt__(self, other):
        return self.val < other.val
    def __lt__(self, other):
        return self.val > other.val
    def __ge__(self, other):
        return self.val <= other.val
    def __le__(self, other):
        return self.val >= other.val
    def __str__(self):
        return ''+str(self.name)+':'+str(self.val);

heap = [];


for i in range(10,0,-1):
    heapq.heappush(heap, node(str(i),i));
    
for n in heap:
    print(str(n));


n = heapq.heappop(heap)
print(str(n));
print();
for n in heap:
    print(str(n));
if __name__ == '__main__':
    pass