# -*- coding: utf-8 -*-
'''
Created on 2018年7月14日

@author: zwp12
'''

'''
使用动态规划实现最优矩阵连乘次序

'''
import numpy as np;



def trace_back(s,i,j):
    if i== j:return ;
    trace_back(s,i,s[i][j]);
    trace_back(s,s[i][j]+1,j);
    # opt ;

def mat_chain_dp(mat_ind,# 矩阵维度数组
                 m,# n*n的DP缓存矩阵
                 s):
    n = len(mat_ind)-1;# 矩阵链中矩阵数
    for r in range(1,n):# 往右上扫描
        for i in range(0,n-r):
            j = i+r;
            # 初始计算m[i][j]为默认分割位置矩阵为[i,i]
            # 因m[i][i]=0，所以省略，增加的计算量为[i,i] 和 [i,j]矩阵的情况
            m[i][j]=m[i+1][j]+ (mat_ind[i]*mat_ind[i+1]) *mat_ind[j+1];
            s[i][j]=i;

            for k in range(i+1,j):
                t = m[i][k]+m[k+1][j]+mat_ind[i]*mat_ind[k+1]*mat_ind[j+1];
                if t < m[i][j]:
                    m[i][j]=t;
                    s[i][j]=k;
            
def run():
    np.random.seed(121212);
    n= 10;
    mat_ind = np.random.randint(5,100,n+1);
    # mat_ind= [30,35,15,5,10,20,25];
    print(mat_ind);
    m = np.zeros((n,n),np.int);
    s = np.zeros([n,n],np.int);
    mat_chain_dp(mat_ind,m,s);
    
    print(m);
    print(s);
    trace_back(s,0,n-1);
    pass;


if __name__ == '__main__':
    run();
    pass