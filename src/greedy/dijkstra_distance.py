# -*- coding: utf-8 -*-
'''
Created on 2018年7月31日

@author: zwp12
'''

'''
 贪心策略的dijkstra求解单源最短路径问题
 
 
 G=(V,E)
 S = {1}
 源到其他顶点的距离origin->dis[j]
 在每次迭代下，
 1.在V-S中选择dis[j]有边且最短的顶点，并将这个顶点加入S集合中
 2.在遍历新的V-S集合来更新dis数组，dis[u]= min(dis[u],dist[k]+e[k][u])
 3.在2中最短路径的前置节点
 进入下次迭代直到V为空集
 
'''
import sys;

MAXINT = sys.maxsize;


def dijkstra(g,origin):
    n = len(g);
    
    S = set([origin]);
    V = set([i for i in range(n)])-S;
    
    dis=[0]*n;# 最短路径
    prev=[-1]*n;# 前置节点
    for it in V:
        dis[it]=g[origin][it];
        if dis[it] != MAXINT:
            prev[it]=origin;

    
    for _ in range(n-1):# 迭代n-1次
        u=origin;tmp=MAXINT;
        for it in V:
            if dis[it]<tmp:
                u=it;tmp=dis[it];
        V.remove(u);
        
        for it in V:
            if g[u][it]<MAXINT :
                newdis = dis[u]+g[u][it];
                if newdis<dis[it]:
                    dis[it]=newdis;
                    prev[it]=u;
    return dis,prev;        
    
    pass;

def run():
    g=[[0,     10,    MAXINT,30,    100],
       [MAXINT,0,     50,    MAXINT,MAXINT],
       [MAXINT,MAXINT,0,     MAXINT,10    ],
       [MAXINT,MAXINT,20    ,0,     60    ],
       [MAXINT,MAXINT,MAXINT,MAXINT,0     ]];
    print(dijkstra(g,0));
    pass;



if __name__ == '__main__':
    run();
    pass