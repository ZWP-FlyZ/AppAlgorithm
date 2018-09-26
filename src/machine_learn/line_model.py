# -*- coding: utf-8 -*-
'''
Created on 2018年9月21日

@author: zwp12
'''

'''

n维特征的回归线性模型
f(x)= w*x+b

'''

import numpy as np;


class line_model():
    w = None;
    feat_size = 0;
    def __init__(self,feat_size):
        self.feat_size=feat_size;
        
    
    def init_weight(self,x,y):
        m = len(x);
        y = np.reshape(y,[-1,1]);
        X = np.concatenate((x,np.ones([m,1],x.dtype)),
                           axis=1);
        xx = np.matmul(X.T,X);
        xx = np.mat(xx).I;
        w = np.matmul(xx,X.T)*y;
        print(w);
        self.w=w;
    
    def f(self,x):
        m=len(x);
        X = np.concatenate((x,np.ones([m,1],x.dtype)),axis=1);
        return np.matmul(X,self.w);



def run():
    
    xy = [[-1.2,-1.9],
          [2.1,1.1],
          [3,1.0]];
    xy = np.array(xy,np.float32);      
    
    f_s = len(xy[0])-1;
    model = line_model(f_s);
    x = xy[:,0:f_s];
    y = np.reshape(xy[:,f_s],[-1,1]);
    model.init_weight(x, y);
    
    nx = np.array([[0],[1]]);
    print(model.f(nx));
    pass;




if __name__ == '__main__':
    run();
    pass