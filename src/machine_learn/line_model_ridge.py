# -*- coding: utf-8 -*-
'''
Created on 2018年9月29日

@author: zwp12
'''

'''
岭回归

'''


import numpy as np;


class line_model_ridg():
    w = None;
    feat_size = 0;
    def __init__(self,feat_size):
        self.feat_size=feat_size;
        
    
    def init_weight(self,x,y,lam=0.2):
        m = len(x);
        y = np.reshape(y,[-1,1]);
        X = np.concatenate((x,np.ones([m,1],x.dtype)),
                           axis=1);
        xx = np.matmul(X.T,X);
        xx+=+lam*np.eye(X.shape[1]);
        # xx 不可逆
        if np.linalg.det(xx) == 0:
            raise ValueError('matirx is singular');
        xx = np.mat(xx).I;
        w = np.matmul(xx,X.T)*y;
        print(w);
        self.w=w;
    
    def f(self,x):
        m=len(x);
        X = np.concatenate((x,np.ones([m,1],x.dtype)),axis=1);
        return np.matmul(X,self.w);



def run():
    
    xy = [[-1,-2],
          [2,1],
          [3,2]];
    xy = np.array(xy,np.float32);      
    
    f_s = len(xy[0])-1;
    model = line_model_ridg(f_s);
    x = xy[:,0:f_s];
    y = np.reshape(xy[:,f_s],[-1,1]);
    model.init_weight(x, y,9.9);
    
    nx = np.array([[0],[1]]);
    print(model.f(nx));
    pass;





if __name__ == '__main__':
    run();
    pass