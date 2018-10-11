# -*- coding: utf-8 -*-
'''
Created on 2018年10月10日

@author: zwp12
'''

'''
softmax 多分类问题

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
    plt.plot(x,y);
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

     
def line_model_softmax(train,learn_param):
    train_x,train_y = train;
    data_size = len(train_x);
    feat_size = len(train_x[0]);
    classif_size = len(train_y[0]);
    lr,batch_size,epon = learn_param;

    # 正态标准化数据集
#     meanx = np.mean(train_x, axis=0);
#     stdx = np.std(train_x,axis=0);
#     train_x = (train_x-meanx)/stdx;
    
    # train_y =  train_y - np.mean(train_y,axis=0);
    

    # 添加x0 和 回归系数
    train_x = np.concatenate([np.ones([data_size,1]),train_x],axis=1);
    w = np.random.normal(0.0,1.0,[classif_size,feat_size+1]);
    # 设置随机提取数据集
    ds = dataset(train_x,train_y);
    ds.random();
    
    for ep in range(epon):
        print('ep=%d start'%(ep+1));
        xy = ds.next(batch_size);
        while xy != None:
            x,y = xy;
            m = y.shape[0];
            py = np.exp(np.matmul(x,w.T));
            py = py/np.sum(py,axis=1,keepdims=True);
            delta = lr/m*(np.matmul((py-y).T ,x));
            w = w- delta;
            mae = np.mean(np.abs(py-y));
#             print('----->\n',w,'\n<--------\n');
            print('mae=%f'%mae);
            xy = ds.next(batch_size);
        ds.random();

    return w;

def predict(w,x):
    data_size = len(x);    
    test_x = np.concatenate([np.ones([data_size,1]),x],axis=1);    
    res =  np.exp(np.matmul(test_x,w.T));
    res = res/np.sum(res,axis=1,keepdims=True);
    return res;

def run():
    
    data_size=150;
    classif=3;
    lx1 = np.random.uniform(-1,0,[data_size,1]);
    ly1 = np.random.uniform(-1,1,[data_size,1]);
    labx1 = np.zeros([data_size,classif]);
    labx1[:,0]=1;
    x1 = np.concatenate([lx1,ly1],axis=1);
    
    lx2 = np.random.uniform(1,2,[data_size,1]);
    ly2 = np.random.uniform(-1,0,[data_size,1]);
    x2 = np.concatenate([lx2,ly2],axis=1);
    labx2 = np.zeros([data_size,classif]);
    labx2[:,1]=1;
    
    
    lx3 = np.random.uniform(0.2,1,[data_size,1]);
    ly3 = np.random.uniform(0.5,1,[data_size,1]);
    x3 = np.concatenate([lx3,ly3],axis=1);
    labx3 = np.zeros([data_size,classif]);
    labx3[:,2]=1;
    
    
    x = np.concatenate([x1,x2,x3],axis=0);
    y = np.concatenate([labx1,labx2,labx3],axis=0);
    
    test=[[-0.5,0],
          [0.5,1],
          [2.6,-0.3]];
    test=np.array(test);

    
    
#     meanx = np.mean(x, axis=0);
#     stdx = np.std(x,axis=0);
#     x = (x-meanx)/stdx;
#     # y =  y - np.mean(y,axis=0);
    set_dataset(x1[:,0],x1[:,1]);
    set_dataset(x2[:,0],x2[:,1]);
    set_dataset(x3[:,0],x3[:,1]);
#     set_dataset(x[:,0],x[:,1]);    
    w = line_model_softmax((x,y),(0.3,3,30));
    print(w);
    nw = np.concatenate([-w[:,1:2]/w[:,2:3],-w[:,0:1]/w[:,2:3]],axis=1);
    print(nw);
    for lin in nw:
        set_line_model(np.linspace(-2,2,20),lin);
    print(predict(w,test));    
    show_fig();
    pass;


if __name__ == '__main__':
    run();
    pass





if __name__ == '__main__':
    pass