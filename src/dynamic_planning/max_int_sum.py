# -*- coding: utf-8 -*-
'''
Created on 2018年7月16日

@author: zwp12
'''

'''
动态规划实现求解最大字段和问题，可以为负整数，



result=max(0,sum),结果最小为0


'''
import numpy as np;
import time ;
def mss_simple(a):
    '''
    O(n*n) 常规方法
    '''
    n = len(a);
    ms=-1;
    me=-1;
    max_sum = 0;
    for i in range(0,n):
        this_sum= 0;
        for j in range(i,n):
            this_sum+=a[j];
            if this_sum>max_sum:
                max_sum=this_sum;
                ms=i;me=j;
    return max_sum,ms,me;




def mss_divid(a,left,right):
    '''
    O(n*logn) 分治法求解问题
    '''
    if left==right:
        if a[left]>0:return a[left];
        else: return 0;
    else:
        cent = int((left+right)/2);
        leftsum=mss_divid(a, left, cent);
        rightsum=mss_divid(a, cent+1, right);
        
        # 计算低三种情况
        s1=0;lefts=0;
        for i in range(cent,left-1,-1):
            lefts+=a[i];
            if lefts>s1:
                s1=lefts;
        
        s2=0;rights=0;
        for i in range(cent+1,right+1):
            rights+=a[i];
            if rights>s2:
                s2=rights;
    
        ### s1 必定小于等于 leftsum
        ### s2 必定小于等于 rightsum
        all_sum = s1+s2;
        if all_sum < leftsum:
            return leftsum;
        elif all_sum < rightsum:
            return rightsum;
        
        return all_sum;
    pass

def mss_dp(a):
    '''
    O(N) 动态规划算法
    '''
    sum=0;b=0;
    n=len(a);
    ss= -1;
    se= -1;
    for i in range(0,n):
        if b>0:b+=a[i];
        else: 
            b = a[i];
            ss = i;
        if b>sum:
            sum=b;
            se=i;
    return sum,ss,se;



def run():
    np.random.seed(121212);
    n = 10000;
    a = np.random.randint(-30,30,n);
    now = time.time();
    # a=[-1,2,3,-4,5]
    # print(mss_simple(a));
    print(mss_divid(a,0,len(a)-1));
    print(mss_dp(a));
    print('time=%.2f'%(time.time()-now));
    pass;

if __name__ == '__main__':
    run();
    pass