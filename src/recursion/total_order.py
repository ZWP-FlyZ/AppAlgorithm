# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: zwp12
'''

'''
用递归思路对n个元素进行全排序

思路：
n=1 f(n) = r
n>1 f(n) = r1-f(R1),r2-f(R2)... rn-f(Rn)

'''
import numpy as np;

def swap(arr,a,b):
    tmp = arr[a];
    arr[a]= arr[b];
    arr[b] = tmp;


def same(arr,k,m):
    for i in range(k,m):
        if arr[i]==arr[m]:
            return True;
    return False;

def order(arr,k):
    m = len(arr);
    if k == (m-1):
        print(arr);
        pass;
    else:
        for i in range(k,m):
            if(same(arr,k,i)):
                continue;
            swap(arr,i,k);
            order(arr,k+1);
            swap(arr,i,k);
            
def run():
    
    li = np.arange(1,6);
    # li = np.array([1,2,3,4]);
    # print(li);
    order(li,0);
    
    pass;


if __name__ == '__main__':
    run();
    pass