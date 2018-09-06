# -*- coding: utf-8 -*-
'''
Created on 2018年9月6日

@author: zwp12
'''

'''
>堆创建与操作
'''


def init_max_heap(arr):
    '''
    >用数组初始化最大堆
    '''
    if arr is None or len(arr)==0:
        raise  ValueError('arr err');
    n = len(arr);
    heap = [0];
    heap.extend(arr);
    for i in range(n//2,0,-1):
        son = i*2;
        heap[0]=heap[i];
        # 循环下找替换调整
        while son<=n:
            if son<n and heap[son]<heap[son+1]:
                son+=1;
            if heap[0]>=heap[son]:
                break;
            else:
                heap[son//2]=heap[son];
                son*=2;
        heap[son//2]=heap[0];
    heap[0]=None;    
    return heap;
    

def max_heap_insert(heap,v):
    n = len(heap);
    heap.append(v);
    son = n;
    while True:
        head = son//2;
        if (head<1 or heap[head]>=v):break;
        heap[0]=heap[head];
        heap[son]=heap[0];
        heap[head]=v;
        son=son//2;
    heap[0]=None;

def max_heap_remove(heap,idx):
    if idx<1 or idx>=len(heap):
        raise ValueError('Err idx');
    n = len(heap)-1;
    v = heap[idx];
    if idx==n:
        heap.pop();
    else:
        heap[idx]=heap[n];
        son=idx*2;n=n-1;
        heap.pop();
        while son<=n:
            if son<n and heap[son]<heap[son+1]:
                son+=1;
            if heap[son//2]>=heap[son]:break;
            else:
                heap[0]=heap[son];
                heap[son]=heap[son//2];
                heap[son//2]=heap[0];
                son*=2;
        heap[0]=None;
    return v;

def heap_sort(arr):
    heap = init_max_heap(arr);
    while len(heap)>1:
        print(max_heap_remove(heap,1));
    pass;
        

if __name__ == '__main__':
    
    
    arr=[4, 1, 3, 2, 16, 9, 10, 14, 8, 7];
    heap = init_max_heap(arr);
    print(heap);
    max_heap_insert(heap,15);
    print(heap);
#     max_heap_remove(heap,5);
#     print(heap);

    print(heap_sort(arr));



    pass