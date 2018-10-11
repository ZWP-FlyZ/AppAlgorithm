# -*- coding: utf-8 -*-
'''
Created on 2018年10月11日

@author: zwp12
'''

'''
带标签类型的聚类方法，学习向量化

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


def svq(data,y,lr,repeat):
    datasize = len(data);
    
        ########## 归一hua # 
        
    mi = np.min(data,axis=0);
    ma = np.max(data,axis=0)
    data=(data-mi)/(ma-mi);
                 
    class_type = list(set(y.tolist()));
    class_idx = {};
    cents=[];
    for ty in class_type:
        class_idx[ty]=np.where(y==ty)[0];
        ci = random.choice(class_idx[ty]);
        cents.append(data[ci]);
    cents=np.array(cents);
    
    data_idx = [i for i in range(datasize)];
    
    for i in range(repeat):
        idx = random.choice(data_idx);
        ditem = data[idx];
        dis = np.sum((cents-ditem)**2,axis=1);
        tagk= np.argmin(dis);
        if class_type[tagk] == y[idx]:
            cents[tagk] =cents[tagk] + lr * (ditem - cents[tagk]);
        else:
            cents[tagk] =cents[tagk] - lr * (ditem - cents[tagk]);
            
    res = [[] for _ in range(len(class_type))];
    for i in range(datasize):
        dis = np.sum((cents-data[i])**2,axis=1);
        tagk= np.argmin(dis);
        res[tagk].append(i);
    cents=cents*(ma-mi)+mi; 
    
    return cents,res;


    
    

def run():
    data_size=200;
    classif=3;

    lx1 = np.random.uniform(-1,0,[data_size,1]);
    ly1 = np.random.uniform(0,1,[data_size,1]);
    x1 = np.concatenate([lx1,ly1],axis=1);
    lab1 =np.full([data_size],0);
    
    lx2 = np.random.uniform(0.5,1.5,[data_size,1]);
    ly2 = np.random.uniform(0,1,[data_size,1]);
    x2 = np.concatenate([lx2,ly2],axis=1);
    lab2 =np.full([data_size],1);
    
    lx3 = np.random.uniform(-0.25,0.75,[data_size,1]);
    ly3 = np.random.uniform(-0.5,0.2,[data_size,1]);
    x3 = np.concatenate([lx3,ly3],axis=1);
    lab3 =np.full([data_size],2);

    y = np.concatenate([lab1,lab2,lab3],axis=0);

    x = np.concatenate([x1,x2,x3],axis=0);
    ridx = np.linspace(0, len(x)-1,len(x),dtype=np.int);
    np.random.shuffle(ridx);
    x = x[ridx];
    y = y[ridx];
    cent,res=svq(x,y,0.1,100);
        
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

