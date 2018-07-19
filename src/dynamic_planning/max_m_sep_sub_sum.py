# -*- coding: utf-8 -*-
'''
Created on 2018年7月18日

@author: zwp12
'''

'''
动态规划解决 m个互不相交的 整数子串和 最大

当m=1 时 退化到mss_dp;

O(m*(n-m))

'''


def mss_m_sep(a,m):
    n = len(a);
    if n<m or m<1:return 0;
    b=[0]*(n+1); # 当前行的结果情况
    c=[0]*(n+1); # 上一行的b(i-1,t) 的最大值
    
    for i in range(1,m+1):
        b[i]=b[i-1]+a[i-1];
        c[i-1]=b[i];
        c_max = b[i];
        for j in range(i+1,i+n-m+1):
            if (b[j-1]>c[j-1]):b[j]=b[j-1]+a[j-1];
            else:b[j]=c[j-1]+a[j-1];
            c[j-1] = c_max;
            if (c_max < b[j]): c_max=b[j];
        c[i+n-m]=c_max;
    
    asum = 0;
    for j in range(m,n+1):
        if asum<b[j]:asum=b[j];
    return asum;
     
    pass;


def run():
    a = [-1,2,3,-4,5];
    m=4;
    print(mss_m_sep(a,m));
    pass;


if __name__ == '__main__':
    run();
    pass