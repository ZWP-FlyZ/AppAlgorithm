# -*- coding: utf-8 -*-
'''
Created on 2018年10月9日

@author: zwp12
'''

'''
梯度下降法求解线性模型回归系数

'''
import numpy as np;

import matplotlib.pyplot as plt 


noise_rou = 1;

def get_origin_model(x):
    return -1.5 * x +2; 
    # return np.exp(x);
def get_lable(x):
    x_s = np.alen(x);
    gas_noise = np.random.normal(scale=noise_rou,size=x_s);
    sin_noise =np.sin(6*x);
    st=1;
    gt=1;
    y = get_origin_model(x);
    return y+st*sin_noise+gt*gas_noise;

def set_dataset(x,y):
    plt.figure(1);
    plt.scatter(x,y);
    oy = get_origin_model(x);
    # plt.plot(x,oy,'b',);
    
def set_line_model(x,w):
    w = np.array(w);
    plt.figure(1);
    y = x * w[0]+w[-1];
    plt.plot(x,y,'r');
    # plt.plot(x,np.exp(y),'y'); 
    pass;
def show_fig():
    plt.show();


class dataset():
    x=None;
    y=None;
    datasize=0;
    order=None;
    start=0;
    bs=0;
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
        self.datasize=len(x);
    
    def random(self):
        self.order=np.arange(self.datasize);
        np.random.shuffle(self.order);
        self.start=0;
    
    def restart(self):
        self.start=0;
    
    def next(self,batch_size=0):
        if self.order is None: raise ValueError('run random() function first');
        self.bs=batch_size;
        # 当batch_size=0时，全部数据返回
        if batch_size==0:
            self.bs =self.datasize;
        # 当到结尾时，无数据返回则返回None
        if self.start>=self.datasize:
            return None;
        else:
            end= min(self.start+self.bs,self.datasize);
            ret = self.x[self.start:end],self.y[self.start:end];
            self.start=end;
            return ret;
        
def line_model_gd(train,learn_param):
    train_x,train_y = train;
    data_size = len(train_x);
    feat_size = len(train_x[0]);
    lr,batch_size,epon,lamda = learn_param;

    # 正态标准化数据集
#     meanx = np.mean(train_x, axis=0);
#     stdx = np.std(train_x,axis=0);
#     train_x = (train_x-meanx)/stdx;
    
    # train_y =  train_y - np.mean(train_y,axis=0);
    

    # 添加x0 和 回归系数
    train_x = np.concatenate([np.ones([data_size,1]),train_x],axis=1);
    w = np.random.normal(0.0,1.0,[feat_size+1,1]);
    w = np.mat(w);
    # 设置随机提取数据集
    ds = dataset(train_x,train_y);
    ds.random();
    
    for ep in range(epon):
        print('ep=%d start'%(ep+1));
        xy = ds.next(batch_size);
        while xy != None:
            x,y = np.mat(xy[0]),np.mat(xy[1]);
            m = y.shape[0];
            py = x*w;
            dtw0 = lr*np.mean(py-y);
            dtwk = lr/m*(x.T * (py-y)+lamda * w);
            w[0,0]=w[0,0]-dtw0;
            w[1:,:]=w[1:,:]-dtwk[1:,:];
            mae = np.mean(np.abs(py-y));
#             print('----->\n',w,'\n<--------\n');
            print('mae=%f'%mae);
            xy = ds.next(batch_size);
        ds.random();

    return w;


def run():
    
    dataset_param=[-5,5,500];
    train_x =  np.linspace(*dataset_param); 
    train_y =  get_lable(train_x);
    
    
    x = np.reshape(train_x,[-1,1]);
    y = np.reshape(train_y,[-1,1]);
    
    
    meanx = np.mean(x, axis=0);
    stdx = np.std(x,axis=0);
    x = (x-meanx)/stdx;
    # y =  y - np.mean(y,axis=0);
    set_dataset(x,y);
    
    
    w = line_model_gd((x,y),(0.02,5,6,0.002));
    w = np.reshape(np.array(w.T),[-1]);
    w = np.concatenate([w[1:],w[0:1]]);
    print(w);
    set_line_model(train_x,w);
    show_fig();
    pass;


if __name__ == '__main__':
    run();
    pass