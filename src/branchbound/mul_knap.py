# -*- coding: utf-8 -*-
'''
Created on 2018年9月19日

@author: zwp12
'''
import numpy as np;
import heapq ;

def reoge(price,special):
    n = len(price);    
    v = np.sum(special[:,0:n]*price,axis=1);
    v = np.reshape(special[:,n],[-1]) / v;
    idx = np.argsort(v);
    return special[idx];


class MinHeapNode():
    dw=0;
    cw=0;
    cp=0;
    lev=0;
    def __init__(self,dw,cw,cp,lev):
        self.dw=dw;
        self.cw=cw;
        self.cp=cp;
        self.lev=lev;
    def __gt__(self, other):
        return self.dw > other.dw
    def __lt__(self, other):
        return self.dw < other.dw
    def __ge__(self, other):
        return self.dw >= other.dw
    def __le__(self, other):
        return self.dw <= other.dw


def addNode(heap, dw,cw,cp,lev):
    node = MinHeapNode(dw,cw,cp,lev);
    heapq.heappush(heap, node);

def branch_bound(op,sp,spe,c):
    n = len(spe);
    item_size=len(op);
    heap=[];
    
    cw=np.zeros([item_size,],np.int);
    cp=0;
    i=0;

    
    # 比较是否小于等于
    def le(a,b):
        for i in range(len(a)):
            if a[i]>b[i]:return False;
        return True;
    # 计算下界
    def bound(j,ccw,ccp):
        if not le(ccw,c):
            return ccp;
        leftc = c - ccw;
        cc = ccp;
 
        while j<n and le(spe[j],leftc):    
            while le(spe[j],leftc):
                cc+=sp[j];
                leftc  = leftc-spe[j];   
            j+=1;
        
        return cc+np.sum(leftc*op);
    
    def cal_cp(ccw,ccp):
        leftc = c - ccw;
        ccp+= np.sum(leftc*op);
        return ccp;
    
    bestp = cal_cp(cw,cp); 
       
    while i<n:
        tmp = cw+spe[i];
        tmp2= cp+sp[i];
        while le(tmp,c):
            tmp2 = cal_cp(tmp,tmp2);
            if(tmp2<bestp): bestp=tmp2;
            addNode(heap,tmp2,tmp,tmp2,i+1);
            tmp+=spe[i];
            tmp2+=sp[i];
        
        # dw = bound(i+1,cw,cp);
#         if dw<bestp:
        tmp2 = cal_cp(cw,cp);
        if bestp> bound(i+1,cw,cp):
            addNode(heap,tmp2,cw,cp,i+1);
        
        if len(heap) == 0:break;    
        
        node = heapq.heappop(heap);
        cw = node.cw;
        cp = node.cp;
        i = node.lev;
         
    return bestp;




class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(price);
        op = np.array(price,np.int32);
        spe = np.array(special,np.int32);
        c = np.array(needs,np.int32);
        nspe = reoge(op,spe);
        return branch_bound(op,nspe[:,n],nspe[:,0:n],c);



if __name__ == '__main__':
    op = np.array([2,3,4],np.int32);
    spe = np.array([[1,1,0,4],[2,2,1,9]],np.int32);
    c = np.array([1,2,1],np.int32);
    print(spe);
    nspe = reoge(op,spe);
    print(nspe);
    
    print(branch_bound(op,nspe[:,3],nspe[:,0:3],c));
    
    
    pass