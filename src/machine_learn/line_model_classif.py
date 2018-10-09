# -*- coding: utf-8 -*-
'''
Created on 2018年10月9日

@author: zwp12
'''

'''
 Logistic线性分类方法
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
            ret = self.x[self.order[self.start:end]],self.y[self.order[self.start:end]];
            self.start=end;
            return ret;
   

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x));

def de_sigmoid(y):
    return y*(1-y);

     
def line_model_classif(train,learn_param):
    train_x,train_y = train;
    data_size = len(train_x);
    feat_size = len(train_x[0]);
    lr,batch_size,epon = learn_param;

    # 正态标准化数据集
#     meanx = np.mean(train_x, axis=0);
#     stdx = np.std(train_x,axis=0);
#     train_x = (train_x-meanx)/stdx;
    
    # train_y =  train_y - np.mean(train_y,axis=0);
    

    # 添加x0 和 回归系数
    train_x = np.concatenate([np.ones([data_size,1]),train_x],axis=1);
    w = np.random.normal(0.0,1.0,[feat_size+1]);
    # 设置随机提取数据集
    ds = dataset(train_x,train_y);
    ds.random();
    
    for ep in range(epon):
        print('ep=%d start'%(ep+1));
        xy = ds.next(batch_size);
        while xy != None:
            x,y = xy;
            m = y.shape[0];
            py = sigmoid(np.sum(x*w,axis=1,keepdims=True));
            depy = de_sigmoid(py);
            dtw = lr/m*((py-y)*depy);
            dtw = np.matmul(x.T,dtw).flatten ();
            w=w-dtw;
            mae = np.mean(np.abs(py-y));
#             print('----->\n',w,'\n<--------\n');
            print('mae=%f'%mae);
            xy = ds.next(batch_size);
        ds.random();

    return w;


def run():
    
    data_size=70;

    lx = np.random.uniform(-1,0,[data_size,1]);
    ly = np.random.uniform(-1,1,[data_size,1]);
    labx1 = np.ones([data_size,1]);
    x1 = np.concatenate([lx,ly],axis=1);
    
    lx = np.random.uniform(1,2,[data_size,1]);
    ly = np.random.uniform(-1,0,[data_size,1]);
    x2 = np.concatenate([lx,ly],axis=1);
    labx2 = np.zeros([data_size,1]);
    
    x = np.concatenate([x1,x2],axis=0);
    y = np.concatenate([labx1,labx2],axis=0);
    
    print()
    
#     meanx = np.mean(x, axis=0);
#     stdx = np.std(x,axis=0);
#     x = (x-meanx)/stdx;
#     # y =  y - np.mean(y,axis=0);
    set_dataset(x[:,0],x[:,1]);
    
    
    w = line_model_classif((x,y),(0.4,4,50));
    w = np.reshape(np.array(w.T),[-1]);
    w = np.concatenate([w[1:],w[0:1]]);
    nw = [-w[0]/w[1],-w[2]/w[1]];
    print(w,nw);
    set_line_model(np.linspace(-2,2,20),nw);

    show_fig();
    pass;


if __name__ == '__main__':
    run();
    pass