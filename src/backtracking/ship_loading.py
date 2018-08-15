# -*- coding: utf-8 -*-
'''
Created on 2018年8月15日

@author: zwp12
'''

'''

利用回溯法求解 双船装载问题

假设两船容量c1,c2的和大于总货物的重量

该问题转换为单船最大化装载问题


'''
import numpy as np;
import copy;


def shipload(w,c):
    n = len(w);
    bestw = 0;# 最优解重量
    bestx=[];# 最优解
    x=[0]*n;# 当前解
    cw=0; # 当前重量
    r=0; # 剩余重
    for i in w:r+=i;
    i=0;
    
    while True:
        while i<n and cw+w[i]<=c:
            cw+=w[i];r-=w[i];
            x[i]=1;i+=1;
            
        if i>=n:
            bestw=max(bestw,cw);
            bestx=copy.deepcopy(x);
                
        else:
            # 进入右子树
            x[i]=0;
            r-=w[i];
            i+=1;
        
        # 减
        while cw+r<=bestw:
            i-=1;
            while i>=0 and x[i]==0:
                r+=w[i];
                i-=1;
            
            if i==-1: return bestw,bestx;
            
            x[i]=0;
            cw-=w[i]
            i+=1;     
        
        #end while i
        
    # end while
    
    
    pass;

def run():
    w = np.random.randint(1,30,100);
    print(shipload(w,40))
    pass;



if __name__ == '__main__':
    run();
    pass