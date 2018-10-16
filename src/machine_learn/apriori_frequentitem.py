# -*- coding: utf-8 -*-
'''
Created on 2018年10月16日

@author: zwp12
'''

'''
利用apriori算法发现调用记录中的频繁项集

'''

def createC1(dataset):
    '''
    >创建数据集中所有物品的单元素集
    '''

    res=[];
    for his in dataset:
        for it in his:
            if([it] not in res):
                res.append([it]);
    res.sort();
    return list(map(frozenset,res))


def createCkp1(Ck,k):
    '''
    >由当前层次Lk,创建包含元素为k的集合列表Ck
    '''
    res = [];
    setsize=len(Ck);
    
    # 以下方法可以避免出现重复的并集
    for i in range(setsize):
        L1 = list(Ck[i])[:k-2];
        for j in range(i+1,setsize):
            L2 = list(Ck[j])[:k-2];
            if L1==L2:
                res.append(sorted(Ck[i] | Ck[j]));
    res = list(map(frozenset,res))
    return res;

def scanD(D,Ck,minsupt):
    '''
    >计算Ck中集合在D中出现的支持度，并选择大于最小支持度的元素
    '''
    cnt={};
    
    # 计算在D中，Ck每一个集合出现的次数
    for his in D:
        for cit in Ck:
            if cit.issubset(his):
                if cit not in cnt:
                    cnt[cit]=1;
                else:
                    cnt[cit]+=1;
    
    res = [];
    supportData={};
    datasize = float(len(D));
    for cit in cnt:
        suprt = cnt[cit]/datasize;
        if suprt>=minsupt:
            res.append(cit);
            supportData[cit]=suprt;
    return res,supportData;


def apriori(dataset,minsupport=0.5):
    C1  = createC1(dataset);
    D = list(map(set,dataset));
    L1,supprtsdata = scanD(D,C1,minsupport);
    L = [L1];
    k=2;
    
    while len(L[k-2])>0:
        Ck = createCkp1(L[k-2],k);
        Lk,supt = scanD(D,Ck,minsupport);
        supprtsdata.update(supt);
        L.append(Lk);
        k+=1;
    L.pop();
    return L,supprtsdata;



def run():
    data = [[1,2],[2,3,4],[1,2,5]];
    
    L,supt = apriori(data);
    print(L[::-1]);
    print(supt); 
    pass;


if __name__ == '__main__':
    run();
    
    
    
    pass