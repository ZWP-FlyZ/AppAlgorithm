# -*- coding: utf-8 -*-
'''
Created on 2018年7月24日

@author: zwp12
'''
'''
通过插入空格使得字符串a,b之间的距离最小

空格和其他字符距离为k

v[m][n] = 
        v[m-1][n-1]   a[m]=b[n]
        
        min{
            v[m-1][n-1]+dis(a[m],b[n]),
            v[m-1][n]+k,
            v[m][n-1]+k
            }


'''

import numpy as np;

k=2;

def dis(ca,cb):
    if ca==' ' or cb==' ':return k;
    else:
        return abs(ord(ca)-ord(cb));
    pass;

def insert_empt(a,b):
    m = len(a)-1;
    n = len(b)-1;
    v = np.zeros((m+1,n+1),np.int);
    # 处理第一行
    for i in range(1,n+1):
        if a[0]==b[i]:v[0][i]=v[0][i-1];
        else:v[0][i]=v[0][i-1]+dis(a[0],b[i]);

    for i in range(1,m+1):
        if a[i]==b[0]:v[i][0]=v[i-1][0];
        else:v[i][0]=v[i-1][0]+dis(a[i],b[0]);


    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i]==b[j]:v[i][j]=v[i-1][j-1];
            else:
                v[i][j]=min(v[i-1][j-1]+dis(a[i],b[j]),
                            v[i-1][j]+k,
                            v[i][j-1]+k);
    return v;


def run():
    a=' cmc';
    b=' snmn';
    
    print(insert_empt(a,b));
    pass;



if __name__ == '__main__':
    run();
    pass