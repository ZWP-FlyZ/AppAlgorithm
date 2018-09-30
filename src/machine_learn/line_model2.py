# -*- coding: utf-8 -*-
'''
Created on 2018年3月30日

@author: zwp
'''
'''
单属性线性回归
'''
import numpy as np
import matplotlib.pyplot as plt 

dataset_param=[0,4,100];
noise_rou = 0.8;
x =  np.linspace(*dataset_param);

def get_origin_model(x):
    return -2 * x +2; 
    # return np.exp(x);
def get_lable(x):
    x_s = np.alen(x);
    gas_noise = np.random.normal(scale=noise_rou,size=x_s);
    sin_noise =np.sin(x);
    st=100;
    gt=0.5;
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

def get_line_w(X,Y):
    X = np.mat(X);
    Y = np.mat(Y);
    # Y = np.log(np.mat(Y));
    xtx = X.T * X;
    w = xtx.I * (X.T * Y);
    return w;


def run():
    y = get_lable(x);
    X = np.reshape(x,[-1,1]);
    X = np.append(X,np.ones([np.alen(x),1]),axis=1);
    Y = np.reshape(y,[-1,1]);
    w = get_line_w(X, Y);
    print(X);
    print(y);
    print(w);
    set_dataset(x, y);
    set_line_model(x, w);
    show_fig();

if __name__ == '__main__':
    run();
    pass