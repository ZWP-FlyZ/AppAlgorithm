# -*- coding: utf-8 -*-
'''
Created on 2018年9月6日

@author: zwp12
'''

import queue;

'''
    单船能够容纳最大货物数
'''

import numpy as np;
import queue;



def enque(q,nw,bestw,i,n):
    if i == n:
        if nw>bestw:
            bestw=nw;
    else:
        q.put(nw);
    return bestw;

def shipload(w,c):
    q = queue.Queue();
    n = len(w)-1;
    bestw=0;
    nw = 0;i=0;
    q.put(-1);
    r=0;
    for k in range(1,len(w)):
        r+=w[k];
    while True:
        wt = nw + w[i];
        if wt<=c:
            if wt>bestw:bestw=wt;
            if i<n:q.put(wt);
        
        if nw+r>bestw and i<n:
            q.put(nw);
        nw = q.get();
        if nw == -1:
            if q.empty():return bestw;
            q.put(-1);
            nw = q.get();
            i+=1;
            r-=w[i];
    pass;

def run():
    
    w = [10,40,40];
    print(shipload(w,50));
    pass;



if __name__ == '__main__':
    run();
    pass