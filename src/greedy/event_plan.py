# -*- coding: utf-8 -*-
'''
Created on 2018年7月29日

@author: zwp12
'''

'''
 贪心算法活动安排方法

分析： 
 越早结束活动使整体时间内的活动量越多
 
 将活动结束时间递增排序，然后后一活动开始时间比前一活动结束晚
'''

def greedy_plan(s,e):
    n = len(s);
    sec = [0]*n;
    sec[0]=1;
    j=0;
    for i in range(1,n):
        if(s[i]>=e[j]):
            sec[i]=1;
            j=i; 
    return sec;
    pass;

def run():
    s=[1,3,0,5,3,5,6,8,8,2,12];
    e=[4,5,6,7,8,9,10,11,12,13,14];
    print(greedy_plan(s,e))
    pass;

if __name__ == '__main__':
    run();
    pass