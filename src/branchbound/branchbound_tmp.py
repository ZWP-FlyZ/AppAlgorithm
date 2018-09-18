# -*- coding: utf-8 -*-
'''
Created on 2018年9月18日

@author: zwp12
'''

'''

最大装载问题拓展模板

单约束条件  和 多约束条件

'''

import heapq;
import copy;

class Bbnode():
    parent=None;
    lchild=0;
    def __init__(self,parent,lchild):
        self.parent=parent;
        self.lchild=lchild;
         
class MaxHeapNode():
    up=0;
    lev=0;
    ptr=None;
    cw=None;
    def __init__(self,up,lev,ptr,cw=None):
        self.up=up;
        self.lev=lev;
        self.ptr=ptr;
        self.cw=cw;
    # 构造极大堆  改变符号
    def __gt__(self, other):
        return self.up < other.up
    def __lt__(self, other):
        return self.up > other.up
    def __ge__(self, other):
        return self.up <= other.up
    def __le__(self, other):
        return self.up >= other.up


def addToHeap(heap,bbnode,up,lchild,lev,cw=None):
    node = MaxHeapNode(up,lev,Bbnode(bbnode,lchild),cw=cw);
    heapq.heappush(heap, node);

def branch_bound(wc,wn,c):
    n = len(wc);
    r=[0]*n;
    if n>1:
        for i in range(n-2,0,-1):
            r[i]=r[i+1]+wc[i+1]*wn[i+1];
        r[0]=r[1]+wc[1]*wn[1];  
              
    i=0;
    cw = 0;
    bbnode=None;# 空父节点
    bestw=0;
    bestx=[0]*n;
    heap=[];
    while i<n:
        k = wn[i];
        while k>0:
            tmp = cw+wc[i]*k;
            if tmp<=c:
                # 添加左节点
                if tmp>bestw:
                    bestw=tmp;
                    besti=i;
                    bestk=k;
                    bestbb=bbnode;
#                 tmp = k*wc[i]+tmp+r[i]; 
                tmp = tmp+r[i];   
                addToHeap(heap,bbnode,tmp,k,i+1);
            k-=1;
            
        # 添加右节点
        if bestw<cw+r[i]:
            addToHeap(heap,bbnode,cw+r[i],0,i+1);
        
        if len(heap)==0:break;
        
        node =  heapq.heappop(heap);
        i = node.lev;
        bbnode = node.ptr;
        cw = node.up - r[i-1] ;
        
        
    cw = bestw;
    i=besti-1;
    bestx[besti]=bestk;  
    bbnode = bestbb;
    while i>=0 :
        bestx[i]=bbnode.lchild;
        bbnode= bbnode.parent;
        i-=1;
            
    return cw,bestx;



def branch_bound_mul(wc,wn,c,opt_tag):
    '''
    >多约束条件
    wc.shape=[约束数目，类数量]
    wn.shape=[类数量]
    c.shape=[约束数目]
    opt_tag:优化目标
    '''
    
    # 约束条件个数
    dim = len(wc);
    
    n = len(wc[0]);
    
    r=[0]*n;
    if n>1:
        for i in range(n-2,0,-1):
            r[i]=r[i+1]+wc[opt_tag][i+1]*wn[i+1];
        r[0]=r[1]+wc[opt_tag][1]*wn[1];  
              
    i=0;
    cw = [0]*dim;
    bbnode=None;# 空父节点
    bestw=0;
    bestx=[0]*n;
    heap=[];
    
    
    # 判断各个约束条件是否满足
    def is_ok(cw,wc,i,k,c):
        for j in range(dim):
            if cw[j]+wc[j][i]*k>c[j]:
                return False;
        return True;
        
    while i<n:
        k = wn[i];
        while k>0:   
            if is_ok(cw,wc,i,k,c):
                # 添加左节点
                # 主优化目标
                tmp = cw[opt_tag]+wc[opt_tag][i]*k;
                if tmp>bestw:
                    bestw=tmp;
                    besti=i;
                    bestk=k;
                    bestbb=bbnode;
                tmp = tmp+r[i];
                # 更新cw
                ncw = copy.deepcopy(cw);
                for j in range(dim):
                    ncw[j]=cw[j]+wc[j][i]*k;   
                addToHeap(heap,bbnode,tmp,k,i+1,ncw);
            k-=1;
            
        # 添加右节点
        if bestw<cw[opt_tag]+r[i]:
            addToHeap(heap,bbnode,cw[opt_tag]+r[i],0,i+1,cw);
        
        if len(heap)==0:break;
        
        node =  heapq.heappop(heap);
        i = node.lev;
        bbnode = node.ptr;
        cw = node.cw;
        
    i=besti-1;
    bestx[besti]=bestk;  
    bbnode = bestbb;
    while i>=0 :
        bestx[i]=bbnode.lchild;
        bbnode= bbnode.parent;
        i-=1;
            
    return bestw,bestx;





if __name__ == '__main__':
    wc=[[16,8,4,2,1],
        [16,16,8,2,1]]
    wn = [2, 1, 4, 3, 5];
    c=[56,128];
    print(branch_bound_mul(wc,wn,c,0));
#     print(branch_bound([16,8,4,2,1],[5,2,4,3,5],56));
    
    pass