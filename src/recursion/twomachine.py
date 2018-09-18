# -*- coding: utf-8 -*-
'''
Created on 2018年8月16日

@author: zwp12
'''

'''
多机流水线 完成时间计算方法

'''
import numpy as np;
import copy;

def swap(arr,a,b):
    tmp = arr[a];
    arr[a]= arr[b];
    arr[b] = tmp;




# np.random.seerandom_alg111);
a = np.random.randint(10,20,[8,5]);
arr = np.arange(0,7);
print(a);
print(arr);

bestt=1000000;
bestx=[];

def order(arr,k):
    global bestt,bestx;
    m = len(arr);
    if k == (m-1):
        tmp=twomachine(a[arr]);
        if tmp<bestt:
            bestt=tmp;
            bestx=copy.deepcopy(arr);
        pass;
    else:
        for i in range(k,m):
            swap(arr,i,k);
            order(arr,k+1);
            swap(arr,i,k);

def twomachine(T):

    # 任务数
    n = len(T);
    # 机器数
    m = len(T[0]);
    
    f = [0]*m;
    
    for i in range(n):
        f[0]+=T[i][0];
        for j in range(1,m):
            if f[j]<f[j-1]:
                f[j]=f[j-1]+T[i][j];
            else:
                f[j]=f[j]+T[i][j];
    return f[-1];
    pass;


def run():

    print(twomachine(a));
    order(arr,0);
    print(bestt,bestx);
    pass;


if __name__ == '__main__':
    run();
    pass