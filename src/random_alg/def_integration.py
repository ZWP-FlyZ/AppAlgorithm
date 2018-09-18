# -*- coding: utf-8 -*-
'''
Created on 2018年9月17日

@author: zwp12
'''

'''
数值随机法求解定积分问题
方法一：面积概率法
方法二：平均法
'''

import random;

def fx(x):
    return x*x+1;

def integration(fx,a,b,n):
    y = 0.0;
    for _ in range(n):
        x = (b-a)*random.uniform(0,1)+a;
        y+=fx(x);
    return (b-a)*y/n;

def run():
    n=1000000;
    print(integration(fx,-1,2,n));

if __name__ == '__main__':
    run();
    pass