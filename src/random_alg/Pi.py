# -*- coding: utf-8 -*-
'''
Created on 2018年9月15日

@author: zwp12
'''

'''
用数值随机化算法计算圆周率
判断随机点对（x,y）落入圆中的概率
近似求解
'''

import random;

def cal_pi(n):
    k=0;
    for _ in range(n):
        x = random.uniform(-1,1);
        y = random.uniform(-1,1);
        if (x*x + y*y)<=1.0 :k+=1;
    return 4.0 * k / n

def run():
    n=90000000;
    print(cal_pi(n));

if __name__ == '__main__':
    run();
    pass