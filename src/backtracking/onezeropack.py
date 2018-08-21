# -*- coding: utf-8 -*-
'''
Created on 2018年8月21日

@author: zwp12
'''


'''

 回溯法求解0-1背包问题
 
 要求输入的权重和重量序列要按照p/w降序排序

'''

import copy;

cp=0;
cw=0;
bestp=0;
bestx=[];


c=10;


w=[5,6,4,2,2];
p=[4,5,6,3,6];


w=[2,2,4,6,5];
p=[6,3,6,5,4];

x=[0]*len(w);

def bound(i):
    lec = c-cp;
    b = cp;
    while i<len(w) and lec>=w[i]:
        b+=p[i];
        lec-=w[i];
        i+=1;
    if i<len(w):
        b+=p[i]*lec/w[i];
    return b;
    

def npk(i):
    global cp,cw,bestp,bestx;
    if(i==len(w)):
        bestp=cp;
        bestx = copy.deepcopy(x);
        return;
    if cw+w[i]<=c:
        cw+=w[i];
        cp+=p[i];
        x[i]=1;
        npk(i+1);
        cw-=w[i];
        cp-=p[i];    
    if bound(i+1)>bestp:
        x[i]=0;
        npk(i+1);
    




def run():
    npk(0);
    print(bestp,bestx);
    
    pass;



if __name__ == '__main__':
    run();
    pass