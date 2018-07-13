# -*- coding: utf-8 -*-
'''
Created on 2018年7月13日

@author: zwp12
'''

'''
递归方法实现分解一个整数为几个正整数的和


'''

def f(m,arr):
    '''
    当前目标数 arr[-1],
    最大分解 m
    '''
    
    n = arr.pop();
    if n==1 :
        return ;
    if n<m:m=n;

    for i in range(n-1,0,-1):
        if i>m:continue;
        j = n - i;
        arr.append(i);
        arr.append(j);
        m=i;
        if m>=j:
            print(arr);
            pass;
        f(m,arr);
        arr.pop();


    pass;


def run():
    
    a = [10];
    f(a[-1],a);

    
    pass;




if __name__ == '__main__':
    run();
    pass