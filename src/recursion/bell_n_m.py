# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: zwp12
'''

'''
bell数， 将n个资源分到m个位置上
规定：每个位置上至少有一个资源
分配方法
例如：将n个元素的集合划分为若干子集

bell 公式
f(n,m)=f(n-1,m-1)+m*f(n-1,m);


将{x}插入到(n-1,m-1)中 和(n-1,m)中
'''

def bell(n,m):
    if m>n or m==0: return 0;
    if n==1 or m==1 or m==n : return 1;
    return bell(n-1,m-1)+m*bell(n-1,m);

def run():
    n=4;
    m=3;
    
    print(bell(n,m));

    pass;



if __name__ == '__main__':
    run();
    pass