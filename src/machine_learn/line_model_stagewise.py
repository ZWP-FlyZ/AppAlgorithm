# -*- coding: utf-8 -*-
'''
Created on 2018年9月30日

@author: zwp12
'''
import sys

'''
前向逐步回归

'''

import numpy as np;
import matplotlib.pyplot as plt 

tag_w=[0.67,-0.0001,0.53,-0.41,0.09,0.0001,0.87];
tag_w= np.reshape(np.array(tag_w),[-1,1]);
batch_size=20;
lr=0.01;step=600;
feat_size=len(tag_w)-1;
np.random.seed(121212121);

err_mu = 0.12;

x = np.random.normal(size=[batch_size,feat_size]);


def get_y(X):
    tx = np.concatenate((X,np.ones([X.shape[0],1])),axis=1)
    err=np.random.normal(0.0,err_mu,[X.shape[0],1]);
    print('norerr\n',err)
    ret =np.matmul(tx,tag_w)+err;
    return ret;

def get_sse(y,py):
    return np.sum((y-py)**2);


def stagewise(x,y,lr,step):
    
    x = np.concatenate((x,np.ones([x.shape[0],1])),axis=1)
    
    n = len(x[0]);
    w = np.ones([n,1],np.float);
    matw=np.zeros([step,n]);
    for i in range(step):
        lowcast=sys.maxsize;
        for feat in range(n):
            for chs in [1,-1]:
                w[feat,0]+=chs*lr;
                py = np.matmul(x,w);
                terr=get_sse(y,py);
                if terr<lowcast:
                    lowcast=terr;
                    bestfeat=feat;
                    bestchs=chs;
                w[feat,0]-=chs*lr;
        w[bestfeat,0]+=bestchs*lr;
        matw[i,:]=np.reshape(w,[-1,]);
        if i%10==0:
            print('step%d,err=%f,bestfeat'%(i+1,lowcast),(bestfeat,bestchs))
    return matw;

def show(wmat):
    step = len(wmat);
    sx = np.arange(step);
    plt.plot(sx,wmat);
    plt.show();

def run():
    print('x\n',x);
    y = get_y(x);
    print('y\n',y);
    
    wmat = stagewise(x,y,lr,step);
    print(wmat);
    print('pw\n',wmat[-1]);
    show(wmat);
    
    



if __name__ == '__main__':
    run();
    pass