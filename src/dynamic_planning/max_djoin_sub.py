# -*- coding: utf-8 -*-
'''
Created on 2018年7月18日

@author: zwp12
'''

'''
动态规划实现最大不相交子集的求解


存在集合{(i,p(i))},i,p(i)属于[1,n]

最小子结构  N(i,j) 而MNS是N的一个子集,表示最大不相交的子集

s[i][j] =   0          i=1 & p(i)<j;
            1          i=1 & p(i)>=j;
            s[i-1][j]  i>1 & p(i)>j;
                                      
            max(    s[i-1][j],        (i,p(i))不在MNS中
                    s[i-1][p(i)-1]+1)    (i,p(i))在MNS中

'''

import numpy as np;

def MNS(a,s):
    n = len(a);
    for i in range(1,n+1):
        if i>=a[0]:s[1][i]=1;
        else:s[1][i]=0;
    for i in range(2,n+1):
        for j in range(1,n+1):
            if a[i-1]>j:s[i][j]=s[i-1][j];
            else:
                s[i][j]=max(s[i-1][j],s[i-1][a[i-1]-1]+1);

def traceback(a,s):
    res = [];
    n = len(a);
    j=n;
    for i in range(n,1,-1):
        if s[i][j] != s[i-1][j]:
            res.append(i);j=a[i-1]-1;
    if (j>=a[0]): res.append(1);
    return res;
    
def run():
    a = [2,3,5,1,4,6,8,7,11,10,9];
    n = len(a);
    s = np.zeros((n+1,n+1),np.int);
    MNS(a,s);
    print(s);
    print(traceback(a,s));
    pass;



if __name__ == '__main__':
    run();
    pass