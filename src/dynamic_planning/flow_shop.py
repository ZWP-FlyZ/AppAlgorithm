# -*- coding: utf-8 -*-
'''
Created on 2018年7月19日

@author: zwp12
'''

'''

动态规划实现   两台机器  流水线处理一批任务的最优调度方案和总时间

johnson法则：假设p为一种排列，a为前置机器的处理时间序列，b为后置机器时间序列
    对于任意 i 属于[i,n-1]中
    min{b[p(i)],a[p(i+1)]}  >=  min{b[p(i+1)],a[p(i)]}
    则p为一种最优方案，实际上对于任意i与j满足上述公式即可 


'''

def flowshop(a,b):
    n = len(a);
    ns1=[];
    ns2=[];
    for i in range(n):
        if a[i]<b[i]:ns1.append([i,a[i]]);
        else:ns2.append([i,b[i]]);
    ns1=sorted(ns1,key=lambda s:s[1]);
    ns2=sorted(ns2,key=lambda s:s[1],reverse=True);
    ns1.extend(ns2);
    c=[s[0] for s in ns1];
    
    j=a[c[0]];
    k=j+b[c[0]];
    for i in range(1,n):
        j+=a[c[i]];
        if j<k:k=k+b[c[i]];
        else: k=j+b[c[i]];
    return k,c;
    pass;



def run():
    a=[3,4,8,10];
    b=[6,2,9,10];
    print(flowshop(a, b));
    pass;

if __name__ == '__main__':
    run();
    pass