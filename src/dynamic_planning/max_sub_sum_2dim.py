# -*- coding: utf-8 -*-
'''
Created on 2018年7月17日

@author: zwp12
'''


'''
动态规划实现求解二维矩阵的最大整数和的子矩阵，可以为负整数，

result=max(0,sum),结果最小为0


'''

import numpy as np;

def mss_dp(a):
    '''
    O(N) 动态规划算法
    '''
    sum=0;b=0;
    n=len(a);
    ss= -1;
    se= -1;
    for i in range(0,n):
        if b>0:b+=a[i];
        else: 
            b = a[i];
            ss = i;
        if b>sum:
            sum=b;
            se=i;
    return sum,ss,se;

def mss_2d_dp(a):
    ''' 
    O(m*m*n) 动态规划方法
    
    1.创建一个行数组b[n],在axis=0方向上逐次累加
    2.每次将b，进行一次一维的mss_dp计算
    
    '''
    
    m = len(a);n=len(a[0]);
    max_sum=0;
    loc=[-1]*4
    for i in range(m):
        b=[0 for _ in range(n)];
        for j in range(i,m):
            b=[b[k]+a[j][k] for k in range(n)];
            s1,x1,x2 = mss_dp(b);
        if max_sum<=s1:
            loc=[i,x1,j,x2];
            max_sum=s1;
    return max_sum,loc;
            
            

    
    
    pass;


def run():
    
    a = [[0,0,0,0],
         [0,1,1,3],
         [0,-2,1,0],
         [0,0,0,2]];
    
    a = np.random.randint(-10,10,(5,5))
    print(a);
    print(mss_2d_dp(a));     
    
    pass;

if __name__ == '__main__':
    run();
    pass