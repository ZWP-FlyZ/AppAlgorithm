# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: zwp12
'''

'''
递归实现快速排序
'''
import numpy as np;

def swap(a,i,j):
    tmp=a[i];
    a[i]=a[j];
    a[j]=tmp;

def part(a,left,right):
    x=a[left];
    i=left;j=right+1;
    while(True):
        while i<right:
            i+=1;
            if a[i]>=x :break;
        while True:
            j-=1;
            if a[j]<=x :break;
        if i>=j:break;
        swap(a,i,j);
    a[left]=a[j];
    a[j]=x;
    return j;
    pass;

def quick_sort(a,left,right):
    if left<right:
        q = part(a,left,right);
        quick_sort(a, left, q-1);
        quick_sort(a, q+1,right);       
    pass;

def run():
    a=np.arange(100000,0,-1);
    b=np.zeros_like(a);
    si = len(a);

    print(a);
    quick_sort(a,0,si-1);
    print(a);
    pass;

if __name__ == '__main__':
    run();
    pass