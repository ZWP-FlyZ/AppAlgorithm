# -*- coding: utf-8 -*-
'''
Created on 2018年10月11日

@author: zwp12
'''

'''
二分Kmeans聚类
'''

import numpy as np;
import random;
import matplotlib.pyplot as plt 

def set_dataset(x,y):
    plt.figure(1);
    plt.scatter(x,y);
    # plt.plot(x,oy,'b',);

def set_dataset_lab(x,y,lab):
    plt.figure(1);
    plt.scatter(x,y,marker=lab);

def show_fig():
    plt.show();


def get_sse(data,cent):
    t = np.sum((data-cent)**2,axis=1);
    t = np.sum(np.sqrt(t));
    return t;


def simple_km(data,k):
    datasize = len(data);
        ########## 归一hua #       
    
    mi = np.min(data,axis=0);
    ma = np.max(data,axis=0)
    ordata = data;
    data=(data-mi)/ma;
    
    if k<1 or  datasize<k:
        raise ValueError('data,k err');
    cents=data[random.sample(range(0,datasize),k)];
    last_c = cents;
    while True:
        res = [[] for _ in range(k)];
        for i in range(datasize):
            dis = np.sum((cents-data[i])**2,axis=1);
            tagk= np.argmin(dis);
            res[tagk].append(i);
        last_c = np.copy(cents);
        for i in range(k):
            cents[i]=np.mean(data[res[i]],axis=0);    
        bout = np.sum(cents-last_c);
        if bout==0:break;
    data=ordata;
    cents=cents*ma+mi;
    sse =[];
    for i in range(len(cents)):
        ct = cents[i];
        cl = data[res[i]];
        sse.append(get_sse(cl,ct));
    return cents.tolist(),res,sse;

def bin_kmeans(data,k):
    cent=[];# 中心列表
    res = [];# 分类结果idx
    sse = [];# sse 暂存
    m = len(data);
    
    res.append([i for i in range(m)]);
    cent.append(np.mean(data,axis=0));
    sse.append(get_sse(data,cent[0]));
    maxsse= sse[0];
    allerr=sse[0];
    print(cent,sse);
    
    while (len(cent)<k):
        lowsse=maxsse;
        besti=-1;
        for i in range(len(cent)):
            tcents,tres,tsse = simple_km(data[res[i]],2);
            spltsse=tsse[0]+tsse[1];
            if allerr-sse[i]+spltsse < lowsse:
                besti=i;
                bestcent=tcents;
                besttres=[[res[i][j] for j in tres[0]] ,[res[i][j] for j in tres[1]]];
                bestsse=tsse;
                lowsse=allerr-sse[i]+spltsse;
        if besti<0:raise ValueError('besti<0 at ',len(cent));
        res[besti:besti+1]=besttres;
        cent[besti:besti+1]=bestcent;
        sse[besti:besti+1]=bestsse;
        allerr = lowsse;
    return cent,res;
    
    

def run():
    data_size=100;
    classif=3;
#     lx1 = np.random.uniform(-1,0,[data_size,1]);
#     ly1 = np.random.uniform(0,1,[data_size,1]);
#     x1 = np.concatenate([lx1,ly1],axis=1);
#     
#     lx2 = np.random.uniform(0.5,1.5,[data_size,1]);
#     ly2 = np.random.uniform(0,1,[data_size,1]);
#     x2 = np.concatenate([lx2,ly2],axis=1);
# 
#     lx3 = np.random.uniform(-0.25,0.75,[data_size,1]);
#     ly3 = np.random.uniform(-0.5,0,[data_size,1]);
#     x3 = np.concatenate([lx3,ly3],axis=1);


    lx1 = np.random.uniform(-1,0,[data_size,1]);
    ly1 = np.random.uniform(0,1,[data_size,1]);
    x1 = np.concatenate([lx1,ly1],axis=1);
    
    lx2 = np.random.uniform(0.5,1.5,[data_size,1]);
    ly2 = np.random.uniform(0,1,[data_size,1]);
    x2 = np.concatenate([lx2,ly2],axis=1);

    
    lx3 = np.random.uniform(-0.25,0.75,[data_size,1]);
    ly3 = np.random.uniform(-0.5,0,[data_size,1]);
    x3 = np.concatenate([lx3,ly3],axis=1);

    x = np.concatenate([x1,x2,x3],axis=0);
    np.random.shuffle(x);
    cent,res=bin_kmeans(x,3);
        
#     cent,res = simple_km(x,3);
    cent=np.array(cent);
     
    print(cent);
    set_dataset_lab(cent[:,0],cent[:,1],'+');
#     print(res);
    for ids in res:
        tx = x[ids];
        set_dataset(tx[:,0],tx[:,1]);
    show_fig();
    pass;

if __name__ == '__main__':
    run();
    pass
