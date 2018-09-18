# -*- coding: utf-8 -*-
'''
Created on 2018年9月15日

@author: zwp12
'''

'''
利用线性同余法产生随机数

'''

import ctypes;
import time;


class RandomNum():
    
    seed = 0;
    
    def __init__(self,seed):
        if seed is None or seed==0:
            self.seed = self.toUnsiged64(int(time.time()*1000));
        else:
            self.seed = self.toUnsiged64(seed);
        self.b = self.toUnsiged64(1194211693);
        self.c = self.toUnsiged64(12345);
    
    def randint(self,n):
        self.seed = self.toUnsiged64(self.b * self.seed + self.c);
        return self.toUnsiged32((self.seed>>32) % n);
        
    def toUnsiged64(self,num):
        return ctypes.c_uint64(num).value;
    def toUnsiged32(self,num):
        return ctypes.c_uint32(num).value;

def run():
    seed = 0;
    res = [0]*10;
    rep=1000000;
    rd = RandomNum(seed);
    for i in range(rep):
        c = rd.randint(10);
        res[c]=res[c]+1;
    print(res);


if __name__ == '__main__':
    run();
    pass