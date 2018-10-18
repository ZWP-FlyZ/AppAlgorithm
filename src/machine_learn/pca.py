# -*- coding: utf-8 -*-
'''
Created on 2018年10月18日

@author: zwp12
'''

'''
利用PCA技术降维
'''

import numpy as np;

def PCA(data,k=0):
    data= np.mat(data);
    mean = np.mean(data,axis=0);
    
    # 中心化
    meandata = data-mean;
    
    # 计算过协方差矩阵
    covdata = np.cov(meandata,rowvar=0);
    # 计算特征值和特征向量
    eigval,eigvect = np.linalg.eig(np.mat(covdata));
    sordedeigidx = np.argsort(eigval);
    print(eigval[sordedeigidx]);
    sordedeigidx = sordedeigidx[:-(k+1):-1]
    redvet = eigvect[:,sordedeigidx];
    # 低维数据
    lowD = meandata * redvet;
    # 重构数据集
    reconMat = (lowD * redvet.T) + mean;
    return np.array(lowD),np.array(reconMat);
    

def run():
    
    np.random.seed(12121212)
    a = np.random.normal(size=[20,5]);
    a[:,4] = a[:,2]*1.8;
    a[:,3] = a[:,2]+0.2;
    print(a)
        
    lowd,recomat = PCA(a,2);
    print(lowd);
    print(recomat);
    
    pass;

if __name__ == '__main__':
    run();
    pass