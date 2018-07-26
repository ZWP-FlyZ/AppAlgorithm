# -*- coding: utf-8 -*-
'''
Created on 2018年7月26日

@author: zwp12
'''

'''
 动态规划实现字符串A变为B的最少编辑次数计算
 编辑包括1.删除 2.添加 3.修改
 
 v[m][n] = 
        n              (m=0)
        m              (n=0)
        v[m-1][n-1]    (A[m]=B[n])
        
        min{           (else)
            v[m-1][n-1]+1    # 修改A[m]字符
            v[m-1][n]+1      # 删除A[m]
            v[m][n-1]+1      # 在A[m]前插入B[n]
        }
  
'''

import numpy as np;

def av_min(li):
    ind = 0;
    vmin = li[ind];
    for i in range(1,len(li)):
        if li[i]<vmin:
            ind=i;vmin=li[i];
    return ind,vmin;
def ED(a,b):
    m = len(a);
    n = len(b);
    v = np.zeros((m+1,n+1),np.int);
    s = np.zeros_like(v);
    for i in range(0,m+1):
        v[i][0]=i;
        s[i][0]=1;
    for i in range(0,n+1):
        v[0][i]=i;
        s[0][i]=2;
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                v[i][j]=v[i-1][j-1];
                s[i][j]=-1;
            else:
                tmp=[v[i-1][j-1],v[i-1][j],v[i][j-1]];
                arg,vm = av_min(tmp);
                s[i][j]=arg;
                v[i][j]=vm+1;
    
    return v,s;

def trackback(s,m):
    pass;
    


def run():
    a='abcde';
    b='bdf';
    v,s = ED(a,b);
    print(v);
    print(s);
    
    pass;

if __name__ == '__main__':
    run();
    pass