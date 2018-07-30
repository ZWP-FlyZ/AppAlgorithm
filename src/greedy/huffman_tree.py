# -*- coding: utf-8 -*-
'''
Created on 2018年7月30日

@author: zwp12
'''

'''
 构建哈夫曼树,过程中采用二叉树和优先队列
'''

import queue as Q;

class BinTreeNode():
    weight=None;
    data=None;
    left=None;
    right=None;
    def __init__(self,weight,data,left,right):
        self.weight=weight;
        self.data=data;
        self.left=left;
        self.right=right;
        
    def __lt__(self,other):
        return self.weight<other.weight;

        pass;
    

class HuffmanTree():
    root = None;
    fes=None;
    code_table=None;
    def __init__(self,fes):
        '''
        fes =[[char,f],[]] 按照f升序排列
        '''
        self.fes=fes;
    
    def build_tree(self):
        que = Q.PriorityQueue();
        for it in self.fes:
            que.put(BinTreeNode(it[1],it[0],None,None));
        while que.qsize()>1:
            a = que.get();
            b = que.get();
            w = a.weight+b.weight;

            que.put(BinTreeNode(w,'',a,b));

        self.root = que.get();    
            
        pass;
    
    def sef(self,node,pt,ct):
        if node.data != '':
            ct.append([node.data,str(pt)])
            return;
        pt.append(0);
        self.sef(node.left,pt,ct);
        pt.pop();
        
        pt.append(1);
        self.sef(node.right,pt,ct);
        pt.pop();        
        
            
    
    def get_code_table(self):
        if self.code_table == None:
            ct = [];pt = [];
            self.sef(self.root,pt,ct);
            
            self.code_table = ct;
        return self.code_table;
        pass;
    pass;



###### END CLASS ########


def run():

    fes = [['f',5],['e',9],['c',12],
           ['b',13],['d',16],['a',45]]

#     fes = [['u',1],['r',1],['i',2],['e',2],
#            ['l',4],['w',4],[' ',5]];
    
    hf = HuffmanTree(fes);
    hf.build_tree();
    print(hf.get_code_table());        
    pass;


if __name__ == '__main__':
    run();
    pass