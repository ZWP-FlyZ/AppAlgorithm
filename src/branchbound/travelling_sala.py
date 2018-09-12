# -*- coding: utf-8 -*-
'''
Created on 2018年9月11日

@author: zwp12
'''



'''
 分支界限法求解旅行商问题


'''

import heapq;



noedge=-1;

class Node():
    dw=0;# 当前节点下界价值
    cc=0;# 当前花费
    rcost=0;# 剩余最小路径
    lev=0;# 当前所在层数
    x=None;# 当前路径
    def __init__(self,dw,cc,rcost,lev,x):
        self.dw=dw;
        self.cc=cc;
        self.rcost=rcost;
        self.lev=lev;
        self.x=x;
    # 构造极大堆  改变符号
    def __gt__(self, other):
        return self.dw > other.dw
    def __lt__(self, other):
        return self.dw < other.dw
    def __ge__(self, other):
        return self.dw >= other.dw
    def __le__(self, other):
        return self.dw <= other.dw





def traveling(g):
    heap = [];
    n = len(g);
    bestc=noedge;
    minout=[0]*n;
    rcost=0;
    for i in range(n):
        tmp=noedge;
        for j in range(n):
            if g[i][j]<tmp or tmp==noedge:
                tmp=g[i][j];
        if tmp==noedge:return noedge;
        minout[i]=tmp;
        rcost+=tmp;
    
    # 初始化 开始节点
    E = Node();
    E.cc=0;
    E.lev=0;
    E.rcost=rcost;
    E.x=[i for i in range(n)]
    
    while E.lev <n-1:
        if E.lev==n-2: # 最后两个城市的处理
            tmp1 = g[E.x[n-2]][E.x[n-1]];
            tmp2 = g[E.x[n-1]][0];
            if tmp1 != noedge and \
                tmp2 != noedge and \
                (E.cc+tmp1+tmp2<bestc or 
                bestc == noedge):
                bestc=tmp1+tmp2+E.cc;
                E.cc=bestc;
                E.dw=bestc;
                E.lev=E.lev+1;
                heapq.heappush(heap, E);
        else:# 寻找可能的后续城市
            
            for i in range(E.lev+1,n):
                if g[E.x[E.lev]][E.x[i]] != noedge:
                    cc = E.cc+g[E.x[E.lev]][E.x[i]];
                    rcost=E.rcost-minout[E.x[E.lev]];
                    dw = cc+rcost;
                    if dw < bestc or bestc == noedge:
                        nx = [E.x[k] for k in range(n)];
                        nx[E.lev+1]=E.x[i];
                        nx[i]=E.x[E.lev+1];
                        N = Node(dw,cc,rcost,E.lev+1,nx);
                        heapq.heappush(heap, N);
        
        # 检查是否还有节点
        if len(heap)==0:break;
        else:E=heapq.heappop(heap);    
            
    if bestc == noedge:return noedge;
    else:
        print(E.x);
        return E.cc;
    

if __name__ == '__main__':
    pass