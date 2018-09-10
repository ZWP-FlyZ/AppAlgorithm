# -*- coding: utf-8 -*-
'''
Created on 2018年9月7日

@author: zwp12
'''


'''

用优先队列分支界限法实现01背包问题

物品预先按照价值重量比从大到小排序


'''

import heapq;

class Knnode():
    up=0;# 当前节点上界价值
    cp=0;# 当前价值
    cw=0;# 当前重量
    lev=0;# 当前所在层数
    def __init__(self,up,cp,cw,lev):
        self.up=up;
        self.cp=cp;
        self.cw=cw;
        self.lev=lev;
    # 构造极大堆  改变符号
    def __gt__(self, other):
        return self.up < other.up
    def __lt__(self, other):
        return self.up > other.up
    def __ge__(self, other):
        return self.up <= other.up
    def __le__(self, other):
        return self.up >= other.up


def bound(w,p,cleft,cp,i):
    n = len(w);
    b = cp;
    while i<n and w[i]<=cleft:
        b+=p[i]; 
        cleft-=w[i];
        i+=1;
        
    if i<n:
        b+=p[i]/w[i]*cleft;
    return b;

def push_node(heap,up,cp,cw,lev):
    node = Knnode(up,cp,cw,lev);
    heapq.heappush(heap, node);


def zero_one_knap(w,p,c):
    
    heap=[];
    n = len(w);
    i=0;cw=0;cp=0;
    bestp=0;
    up=bound(w,p,c-cw,cp,i); 
    
    while i<n:
        if cw+w[i]<=c:
            if cp+p[i]>bestp:bestp=cp+p[i];
            push_node(heap,up,cp+p[i],cw+w[i],i+1);
        up = bound(w,p,c-cw,cp,i+1); 
        if up>bestp:
            push_node(heap,up,cp,cw,i+1);
        
        if len(heap)==0:return bestp;    
        node = heapq.heappop(heap);
        cw = node.cw;
        cp = node.cp;
        up = node.up;
        i = node.lev;
    
    return bestp;    


def run():
    w=[2,2,4,6,5];
    p=[6,3,6,5,4];
    c = 10;
    print(zero_one_knap(w,p,c))
    pass;



    
if __name__ == '__main__':
    run();
    pass