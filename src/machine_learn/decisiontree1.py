# -*- coding: utf-8 -*-
'''
Created on 2018年4月21日

@author: zwp
'''
import operator

'''
    多分类决策树，包含m个属性，每个属性可包含若干个属性值
'''
import math;



def getMostClass(classList):
    '''
    获取classList中，占比最多的类型
    '''
    classcout={};
    for c in classList:
        if c not in classcout:
            classcout[c]=0;
        classcout[c]+=1;
    glist = sorted(classcout.items(),
                   key=operator.itemgetter(1),
                   reverse=True);
    print(glist);
    return glist[0][0];


def calH(dataset):
    '''
    计算dataset的香农熵
    '''
    all_size = len(dataset);
    pcot = {};
    for item in dataset:
        lable = item[-1];
        if lable not in pcot:
            pcot[lable]=0;
        pcot[lable]+=1;
    h = 0;
    for _,cot in pcot.items():
        p = cot *1.0 / all_size;
        h -= p * math.log(p,2); 
    return h;

def splitDataset(dataset,feature,value):
    '''
    将原数据集dataset，提取出feature=value部分
    '''
    retset = [];
    for item in dataset:
        if item[feature]==value:
            newitem = item[:feature];
            newitem.extend(item[feature+1:]);
            retset.append(newitem);
    return retset;
    pass;

def chooseBestFeature(dataset):
    '''
    从dataset中选出使得分割后
    信息熵最小的特征序号
    '''
    all_size = len(dataset);
    feature_size = len(dataset[0])-1;
    baseH = calH(dataset);
    bestFeatureH=0.0;bestFeatureId=-1;
    for fid in range(feature_size):
        flist = [item[fid] for item in dataset];
        flist= set(flist);
        newH = 0.0;
        for fvalue in flist:
            rem_dataset = splitDataset(dataset, fid, fvalue);
            rem_h = calH(rem_dataset);
            p = len(rem_dataset)/float(all_size);
            newH+=p*rem_h;
        subH = baseH-newH;
        if subH > bestFeatureH:
            bestFeatureH = subH;
            bestFeatureId = fid;
    return bestFeatureId;
             
    
def createDecisionTree(dataset,features):
    '''
    递归创建一个决策树，
    dataset:当前递归层次数据集
    features:当前递归层次的特征名数组
    '''
    classList = [item[-1] for item in dataset];
    
    # 当前数据集只包含一种标签类型时返回
    if classList.count(classList[0]) == len(dataset):
        return classList[0];
    
    # 当前数据以删除完所有特征，只包含标签列表时，
    # 返回标签列表中最多的类型名
    if len(dataset[0]) == 1:
        return getMostClass(classList);
     
    bestFeatId = chooseBestFeature(dataset);
    bestFeat = features[bestFeatId];
    del(features[bestFeatId]);
    dtree={bestFeat:{}};
    
    fvalue = [item[bestFeatId] for item in dataset];
    fvalue = set(fvalue);
    for v in fvalue:
        dtree[bestFeat][v]=\
        createDecisionTree(splitDataset(dataset, bestFeatId, v),features.copy());
    return dtree;

def classify(decisionTree,features,testVec):
    '''
    根据决策树进行分类
    decisionTree:决策树
    features:标签名数组
    testVec:测试分类特征向量
    '''
    upfeat = list(decisionTree.keys())[0];
    featid = features.index(upfeat);
    target_fvalue = testVec[featid];
    downDic = decisionTree[upfeat][target_fvalue];
    if type(downDic).__name__ == 'dict':
        classLable = classify(downDic,features,testVec);
    else: classLable = downDic;
    return classLable;

def storeTree(tree,fname):
    import pickle;
    fw = open(fname,'bw');
    pickle.dump(tree,fw);
    fw.close();

def loadTree(fname):
    import pickle;
    fr = open(fname,'br');
    return pickle.load(fr);

def test():
    data=[[1,0,2],
          [3,0,0],
          [3,1,1],
          [1,1,1],
          [2,1,2],
          [2,0,1]]
#     print(calH(data));
#     print(splitDataset(data,1, 2))
#     print(chooseBestFeature(data));
#     getMostClass([1,2,3,4,1,2,1,1,2]);
    dtree = createDecisionTree(data, ['x1','x2']);
    print(dtree);
    print(classify(dtree,['x1','x2'],[3,1]));
    storeTree(dtree,'tree');
    dtree2 = loadTree('tree');
    print(classify(dtree2,['x1','x2'],[3,1]));
    pass;
    

if __name__ == '__main__':
    test();
    pass