# -*- coding: utf-8 -*-
'''
Created on 2018年8月20日

@author: zwp12
'''

'''
 回溯法求解n后放置问题
 
'''



res=0;

def place(x,k):
    for i in range(1,k):
        if(abs(i-k)==abs(x[i]-x[k]) or x[i]==x[k]):
            return False;
    return True;
        
def nqe(x,i):
    global res;
    if i==len(x): 
        res+=1;
        print(x);
    else:
        for k in range(1,len(x)+1):
            x[i]=k;
            if(place(x,i)):nqe(x,i+1);

def run():
    n = 5;
    x = [0]*(n+1);
    nqe(x,1);

if __name__ == '__main__':
    run();
    pass