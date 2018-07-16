# -*- coding: utf-8 -*-
'''
Created on 2018年7月16日

@author: zwp12
'''

'''
动态规划实现寻找最长公共子序列的算法

长度为m的数组a,长度为n的数组b

shape(v)=(m+1,n+1) 0行0列表示空字符串

v[i][j] = 
        0                i=0或者j=0
        v[i-1][j-1]+1    i=j
        max(v[i-1][j],v[i][j-1]) j n_q i


'''
import numpy as np;

def lcs(a,b,v,flag):
    '''
    a,b 字符串
    i,j 分别在a,b上的index ,有效index从1开始
    v DP记录表
    '''
    m = len(a);n=len(b);
    for i in range(0,m):
        for j in range(0,n):
            if (a[i]==b[j]):
                v[i+1][j+1]=v[i][j]+1;
                flag[i+1][j+1]=1;
            elif(v[i][j+1]>v[i+1][j]):
                v[i+1][j+1]=v[i][j+1];
                flag[i+1][j+1]=2;
            else:
                v[i+1][j+1]=v[i+1][j];
                flag[i+1][j+1]=3;
    pass;

def showLSC(i,j,a,b,flag):
    if (i==0 or j==0):return ;
    if (flag[i][j]==1):
        showLSC(i-1,j-1,a,b,flag);
        print(a[i-1],end=' ');
    elif(flag[i][j]==2):
        showLSC(i-1,j,a,b,flag);
    else:
        showLSC(i,j-1,a,b,flag);
    



def run():
    a = [1,2,3,4,4,5,6,7,9,10];
    b = [1,3,11,4,4,12,13,9];
    m = len(a);n=len(b);
    v = np.zeros((m+1,n+1),np.int);
    flag = np.zeros_like(v, np.int);
    lcs(a,b,v,flag);
    print(v);
    print(flag);
    showLSC(m,n,a,b,flag);
    
    pass;


if __name__ == '__main__':
    run();
    pass