# -*- coding: utf-8 -*-
'''
Created on 2018年10月17日

@author: zwp12
'''

'''
利用FPgrowth算法发现频繁项集
'''



class Node():
    
    '''
    FP树节点结构
    '''
    
    name=None;#节点名
    count=0;# 元素出现次数计数
    next=None;#相似节点指针
    parent=None;#父节点
    children=None;# 子节点表
    def __init__(self,name,cnt,parent):
        self.name=name;
        self.count=cnt;
        self.parent=parent;
        self.children={};
    
    def inc(self,numcnt):
        self.count += numcnt;
    
    def show(self,idx=1):
        print('-'*idx,self.name,' ',self.count);
        for child in self.children.values():
            child.show(idx+1);
    

def addToHeadTable(headNode,tagNode):
    while headNode.next != None:
        headNode=headNode.next;
    headNode.next = tagNode;

def updateTree(items,tree,headTable,count,i):
    if items[i] in tree.children:
        # 如果已经存在第i个元素则更新计数
        tree.children[items[i]].inc(count);
    else:
        # 如果不存在，则在当前树的孩子表中添加
        tree.children[items[i]] = Node(items[i],count,tree);
        
        # 更新头节点表
        if headTable[items[i]][1] == None:
            # 创建
            headTable[items[i]][1] = tree.children[items[i]];
        else:
            # 添加
            addToHeadTable(headTable[items[i]][1],tree.children[items[i]]);

    if i < len(items)-1:
        # 如果还有元素，继续迭代
        updateTree(items, tree.children[items[i]],headTable,count,i+1);
            
def createFPtree(dataset,minsup=1):
    '''
    >由数据集创建FP树
    dataset:是一个以记录集为key，记录集出现次数为value的字典。
    minsup:最小支持度，这里是单元素出现次数
    '''
    
    headTable={};# 头指针表
    
    # 第一次遍历数据集，记录单元素出现的次数
    for data in dataset:
        v =  dataset[data];
        for it in data:
            headTable[it] = headTable.get(it,0)+v;
        
    # 清除非频繁的元素
    rmitems=[];
    for k in headTable.keys():
        if headTable[k]<minsup:
            rmitems.append(k);
    for k in rmitems:
        del(headTable[k]);
    
    # 如果无频繁项，结束
    freqItems = set(headTable.keys());
    if len(freqItems)==0:return None,None;
    
    # 添加指针
    for k in headTable:
        headTable[k]=[headTable[k],None];
    
    # FP根节点
    root = Node('Root Null set',1,None);
    for data,count in dataset.items():
        locD = {};# 获得单记录的数据集
        for item in data:
            if item in freqItems:
                # 清除非频繁项
                locD[item]=headTable[item][0];
        
        if len(locD) >0:
            
            # 将剩余元素按计数非减排序
            orded = [v[0] for v in sorted( locD.items(),
                    key=lambda p:p[1],reverse=True )];
            print(orded);
            updateTree(orded, root, headTable, count, 0);
    
    return root,headTable;


def backAccTree(child):
    '''
    >回溯获得父节点列表
    '''
    parents=[];    
    # 去掉自身节点
    child = child.parent;
    while child.parent != None:
        parents.append(child.name);
        child = child.parent;
#     parents.pop(0);
    return parents;


def findPrefixPath(headNode):
    '''
     通过频繁元素的头节点，寻找该元素的前缀路径
    '''
    conpattn = {} # 条件模式基
    while headNode != None:
        prefixpth = backAccTree(headNode);
        print(prefixpth);
        if len(prefixpth)>0:
            conpattn[frozenset(prefixpth)] = headNode.count;
        headNode= headNode.next;
    return conpattn;
        


def mineTree(tree,headTable,minsup,prefix,freqItems):
    bigL = [v[0] for v  in sorted(headTable.items(),
                                key=lambda p:p[1][0])];
    print(bigL);
    for elem in bigL:
        newFrqset= prefix.copy();
        newFrqset.add(elem);
        freqItems.append(newFrqset);
        condPatt = findPrefixPath(headTable[elem][1]);
        condtree,conHead = createFPtree(condPatt, minsup);

        if conHead != None:
            print('condtree for ',newFrqset);
            condtree.show();
            mineTree(condtree,conHead,minsup,newFrqset,freqItems);

def initDataset(dataset):
    ret = {};
    for it in dataset:
#         it.sort(reverse=True);
        k = frozenset(it);
        ret[k] = ret.get(k,0)+1;
    return ret;

            
def run():
    
    data = [['r','z','h','j','p'],
            ['z','y','x','w','v','u','t','s'],
            ['z'],
            ['r','x','n','o','s'],
            ['y','r','x','z','q','t','p'],
            ['y','z','x','e','q','s','t','m']]
    
    initdata = initDataset(data);
    print(initdata);
    
    
    tree,head = createFPtree(initdata,3);
    tree.show();
    
    
#     conpatt = findPrefixPath(head['r'][1]);
#     print(conpatt);
    
    freqItems=[];
    mineTree(tree,head,2,set([]),freqItems);
    print(freqItems);
    
    pass;        



if __name__ == '__main__':
    run();
    pass