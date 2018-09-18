# -*- coding: utf-8 -*-
'''
Created on 2018年7月19日

@author: zwp12
'''

'''
动态规划0-1背包问题

m(i,j) = 
        max{ m(i+1,j),m(i+1,j-wi)} j>=wi
        m(i+1,j) j<wi
         
m(n,j) = 
        vn j>=wn
        0  j<wn


'''

import numpy as np;

def z1_kp(w,v,c):
    n=len(w)-1;
    m = np.zeros((n+1,c+1),np.int);
    for i in range(w[n],c+1):
        m[n][i]=v[n];
    
    for i in range(n-1,-1,-1):
        ins = min(w[i]-1,c);
        for j in range(1,ins+1):m[i][j]=m[i+1][j];
        for j in range(w[i],c+1):
                m[i][j]=max(m[i+1][j],m[i+1][j-w[i]]+v[i]);
    return m;
    pass;

def get_x(m,w,c):
    n = len(w)-1;
    res = [0]*n;
    for i in range(1,n):
        if m[i][c]!=m[i+1][c]:
            res[i-1]=1;
            c-=w[i];
    if m[n][c]!=0:res[n-1]=1;
    return res;
        

def run():
    n=5;
#     w=np.random.rrandom_alg(1,6,n+1);
#     v=np.random.rrandom_alg(2,9,n+1);
    w=[2,2,6,5,4];
    v=[6,3,5,4,6];
    c=10;
    m=z1_kp(w,v,c);
    print(m);
    print(w);
    print(v);
    print(get_x(m,w,c));
    print(m[0][c]);
    pass;

if __name__ == '__main__':
    run();
    pass