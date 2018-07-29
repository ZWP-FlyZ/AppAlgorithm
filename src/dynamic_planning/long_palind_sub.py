# -*- coding: utf-8 -*-
'''
Created on 2018年7月29日

@author: zwp12
'''

'''
 动态规划实现最长回文串
 
    p(i,j) = p(i+1,j-1) & a[i]==a[j]
    // 初始化 p(i,i)=true p(i,i+1)=a[i]==a[i+1]

 
'''

import numpy as np;

def longest_palind(s):
    n = len(s);
    if n<2:return s;
    #  p=[[False]*n]*n;
    p=np.zeros((n,n),bool);
    max_l=0;max_r=0;
    for i in range(0,n-1):
        p[i][i]=True;
        if s[i]==s[i+1] and (max_r-max_l)<1:
            max_l=i;max_r=i+1;
            p[i][i+1]=True;
    
    
    for k in range(2,n):
        for i in range(0,n-k):
            j=i+k;
            p[i][j]=p[i+1][j-1] and s[i]==s[j];
            if p[i][j] and (j-i) > (max_r-max_l):
                max_r=j;max_l=i;
    
    print(p);
    return s[max_l:max_r+1];
    pass;


def run():
    print(longest_palind('cabbaktkabbat'))
    pass;


if __name__ == '__main__':
    run();
    pass