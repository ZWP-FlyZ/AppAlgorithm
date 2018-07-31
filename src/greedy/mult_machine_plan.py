# -*- coding: utf-8 -*-
'''
Created on 2018年7月31日

@author: zwp12
'''

'''
 贪心策略处理n个任务m机器的多机调度
 
 相同机器处理不可分割的不同任务调度方案 时NP完全问题，
 可以用贪心获得近似解
 t表示各个任务处理时间
 
 当n<=m时, 全部放入机器
 当n>m时，将t降序排列，先依次排满m台机器，
 再将剩余任务放入当前最小
 
 
 可以使用最小堆提升效率，这里只采用传统思路O(n*n)
 
'''

def min_ind(arr):
    ti=0;
    tm=arr[ti];
    for i in range(1,len(arr)):
        if arr[i]<tm:
            ti=i;tm=arr[i];
    return tm,ti;

def machine_plan(t,m):
    n = len(t);
    if n<=m:
        return (max(t),None);
    
    t= sorted(t,key=lambda s:s[1],reverse=True);

    plan = [];
    mac_time=[];
    
    for i in range(m):
        plan.append([t[i][0]]);
        mac_time.append(t[i][1]);
    
    for i in range(m,n):
        _,ind = min_ind(mac_time);
        plan[ind].append(t[i][0]);
        mac_time[ind]+=t[i][1];
    
    
    return max(mac_time),plan;
    pass;


def run():
    task=[[1,2],[2,14],[3,4],
          [4,16],[5,6],[6,5],[7,3]];
    machine=3;
    mt,plan=machine_plan(task,machine);
    print(mt);
    print(plan);
    pass;

if __name__ == '__main__':
    run();
    pass