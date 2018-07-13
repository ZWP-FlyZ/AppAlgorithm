# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: zwp12
'''

'''
递归实现合并排序算法

'''
import numpy as np;

def merge(a,b,left,mid,right):
    '''
    等长数组a,b
    '''
    # a=[left...mid]
    # b=[mid+1...right]
    i = left;
    j = mid+1;
    for k in range(left,right+1):
        if i == mid+1:
            b[k]=a[j];j+=1;
        elif j == right+1:
            b[k]=a[i];i+=1;
        elif a[i]<=a[j]:
            b[k]=a[i];i+=1;
        else:
            b[k]=a[j];j+=1;      

def copy(tag,origin,left,right):
    for k in range(left,right+1):
        tag[k]=origin[k];


def merge_sort(a,b,left,right):
    mid = int((left+right)/2);
    if left<right:
        merge_sort(a,b,left,mid);
        merge_sort(a,b,mid+1,right);
        merge(a,b,left,mid,right);
        copy(a,b,left,right);
    pass;



def run():
    a=np.arange(9000,0,-1);
    b=np.zeros_like(a);
    si = len(a);
    np.sort(a);
    print(a);
    merge_sort(a,b,0,si-1);
    print(a);
    
    pass;

if __name__ == '__main__':
    run();
    pass