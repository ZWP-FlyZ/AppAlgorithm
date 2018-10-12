# -*- coding: utf-8 -*-
'''
Created on 2018年10月12日

@author: zwp12
'''

'''
DBSCAN密度聚类方法

'''


import numpy as np;
import random;
import queue ;
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


def dist(x,y):
    return np.sqrt(np.sum((x-y)**2,axis=1));

def dbscan(data,e,MinPts):
    datasize = len(data); 
    Ne = [];# e-邻域
    W = [];# 核心对象集合
    T = np.zeros([datasize]);# 调用记录，1表示以调用
    k=0;# 簇计数器
    Que = queue.Queue();
    
    
    for i in range(datasize):
        tmp =dist(data,data[i]);
        idx = np.where(tmp<=e)[0];
        Ne.append(idx);
        if len(idx)>=MinPts:
            W.append(i);
    res=[];
    while len(W)>0:
        # 仍有核心对象时继续
        # 随机选择一个核心对象
        core_ii = random.randint(0,len(W)-1);
        core_i = W[core_ii];
        Que.put(core_i);
        # 记录当前未调用记录
#         To[:] = T[:];
        T[core_i]=1;
        Ck = [core_i];
        while  not Que.empty():
            # 队列非空继续广度查找
            core_i = Que.get();
            ne = Ne[core_i];
            if len(ne)>=MinPts:
                ti = np.where(T[ne]==0)[0];#取出ne中未被使用的部分
                if len(ti)<1:continue;
                delta = ne[ti];# 还原正确index
                for exp in delta:
                    Que.put(exp);
                    T[exp]=1;
                    Ck.append(exp);
        k+=1;
        res.append(Ck);
        for i in Ck:
            try:W.remove(i);
            except ValueError:pass;
    
    cents=[];
    for ck in res:
        cents.append(np.mean(data[ck],axis=0));
            
    return cents,res;        
                    

def run():
    data_size=200;
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

#     random.seed(12121211);
#     np.random.seed(12121211);
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
    
    print(x);
    
    cent,res=dbscan(x,0.095,4);
        

    cent=np.array(cent);
    print(cent);
    set_dataset_lab(cent[:,0],cent[:,1],'+');
    for ids in res:
        tx = x[ids];
        set_dataset(tx[:,0],tx[:,1]);
    show_fig();
    pass;

if __name__ == '__main__':
    run();
    pass

