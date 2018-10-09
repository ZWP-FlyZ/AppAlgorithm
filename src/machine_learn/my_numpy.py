# -*- coding: utf-8 -*-
'''
Created on 2018年10月8日

@author: zwp12
'''

'''
模拟numpy的一些操作
'''
import copy;


def deepcopy(x):
    return copy.deepcopy(x);

class marray():
    
    '''
    >数据类，
    >data=[marray,....] or [int,] or [float]
    >外层是一个list,
    '''
    shape=None;#数组形状
    data=None;#数据主体
    dtype=None;#数据类型
    def __init__(self,data,shape,dtype):
        self.data=deepcopy(data);
        self.shape=shape;
        self.dtype=dtype;
    
    def __len__(self):
        # 返回第一维长度
        return self.shape[0];
    
    def __getitem__(self, index):
        if isinstance(index,int) :
            # 单选处理
            return self.data[index];
        elif isinstance(index,slice):
            # 单切片处理
            dl = index.stop-index.start;
            if dl<1: raise ValueError('Error slice length lt 1!');
            sp = [dl];
            if len(self.shape)>1:
                sp.extend(self.data[index.start].shape);
            return marray(self.data[index],sp,self.dtype); 
        else:
            # 多选、多切片处理,暂时不支持
            raise TypeError('Error index type ',type(index));
#             print(index);
#             print(len(index));
#             if len(index)>len(self.shape):
#                 raise ValueError('Error slice cot %d most is %'%(len(index),len(self.shape)));
#             ret = self.data;
#             ret_sp = [];
#             op_idx = 0;
#             op = index[op_idx];
#             if isinstance(op, int):
#                 ret_sp.append(1);
#                 ret = ret[op:op+1];
#             else:
#                 ret_sp.append(op.stop-op.start);
#                 ret = ret[op];
#             for op_idx in range(1,len(index)):
#                 pass    
#             return ret;
            # isinstance(index,slice):
            

    def __setitem__(self, index, value):
        # print(type(index));
        if isinstance(index, int):
            # 重置一个元素
            if len(self.shape)>1 and type(self) == type(value):
                # marray 更新
                if value.dtype != self.dtype :
                    raise TypeError('Error value dtype=',value.dtype);
                if value.shape[0] != self.data[index].shape[0] :
                    raise TypeError('Error value shape=',value.shape);
                self.data[index] = deepcopy(value);
            elif len(self.shape)==1 and self.dtype == type(value):
                # 基础类型更新
                self.data[index] = value;
            else:
                raise TypeError('Error value type ',type(value));
        elif isinstance(index,slice) and isinstance(value, marray):
            # 切片重置
            raise TypeError('Error index type ',type(index));
        
#             if index.stop-index.start != len(value):
#                 raise TypeError('Error slice length=',index);
#             
#             self.data[index] = value; 
#         else:
#             raise TypeError('Error value type is',type(value));
        else:
            raise TypeError('Error index type ',type(index));
        
        
    ############################### 运算 ##############################
    def __neg__(self):
        # 所有元素求负
        nself = copy.deepcopy(self); 
        nself.data=list(map(lambda x:-x,nself.data));
        return nself;
    
    def __add__(self, obj):
        # 右加
        if not isinstance(obj,marray) and \
            self.dtype != type(obj):
            raise TypeError('Error data type ',type(obj),' op need marray or ',self.dtype);
        
        if self.dtype == type(obj):
            # 基础类型时全相加
            nself = copy.deepcopy(self);
            nself.data=list(map(lambda x:x+obj,nself.data));
            return nself;
        else:
            if self.dtype != obj.dtype:
                raise TypeError('Error data type ',obj.dtype, ' but origin type is ',self.dtype);
            
            if len(self.shape) == len(obj.shape):
                # 相同时张量阶数时，是各个位置元素相加
                nself = copy.deepcopy(self);
                for i in range(len(self.shape)):
                    if self.shape[i] != obj.shape[i]:
                        raise ValueError('Error data shape ',obj.shape,' but origin shape is ',self.shape);
                nself.data=list(map(lambda x,y:x+y,nself.data,obj.data));    
                return nself;
            # 不同阶数时
            elif len(self.shape) > len(obj.shape):
                a = self;
                b = obj;
            else:
                a = obj;
                b = self;
            nself = copy.deepcopy(a);
            for i in range(nself.shape[0]):
                nself.data[i]=nself.data[i]+b;
            return nself;

    def __radd__(self, other):
        # 左加
        return self.__add__(other);
        
    def __sub__(self, obj):
        # 正向减
        if not isinstance(obj,marray) and \
            self.dtype != type(obj):
            raise TypeError('Error data type ',type(obj),' op need marray or ',self.dtype);
        
        if self.dtype == type(obj):
            nself = copy.deepcopy(self);
            nself.data=list(map(lambda x:x-obj,nself.data));
            return nself;
        else:
            if self.dtype != obj.dtype:
                raise TypeError('Error data type ',obj.dtype, ' but origin type is ',self.dtype);
            if len(self.shape) == len(obj.shape):
                # 相同时张量阶数时，是各个位置元素相加
                nself = copy.deepcopy(self);
                for i in range(len(self.shape)):
                    if self.shape[i] != obj.shape[i]:
                        raise ValueError('Error data shape ',obj.shape,' but origin shape is ',self.shape);
                nself.data=list(map(lambda x,y:x-y,nself.data,obj.data));    
                return nself;
            # 不同阶数时
            elif len(self.shape) > len(obj.shape):
                a = self;
                b = obj;
                nself = copy.deepcopy(a);
                for i in range(nself.shape[0]):
                    nself.data[i]=nself.data[i]-b;
                return nself;
            else:
                a = obj;
                b = self;
                nself = copy.deepcopy(a);
                for i in range(nself.shape[0]):
                    nself.data[i]=b-nself.data[i];
            return nself;

    def __rsub__(self, obj):
        return -self.__sub__(obj);
    
    def __mul__(self, obj):
        if not isinstance(obj,marray) and \
            self.dtype != type(obj):
            raise TypeError('Error data type ',type(obj),' op need marray or ',self.dtype);
        
        if self.dtype == type(obj):
            # 基础类型全部数据相乘
            nself = copy.deepcopy(self);
            nself.data=list(map(lambda x:x*obj,nself.data));
            return nself;
        else:
            if self.dtype != obj.dtype:
                raise TypeError('Error data type ',obj.dtype, ' but origin type is ',self.dtype);
            if len(self.shape) == len(obj.shape):
                # 相同时张量阶数时，是对应位置元素相乘
                nself = copy.deepcopy(self);
                for i in range(len(self.shape)):
                    if self.shape[i] != obj.shape[i]:
                        raise ValueError('Error data shape ',obj.shape,' but origin shape is ',self.shape);
                nself.data=list(map(lambda x,y:x*y,nself.data,obj.data));    
                return nself;
            # 不同阶数时
            elif len(self.shape) > len(obj.shape):
                a = self;
                b = obj;
            else:
                a = obj;
                b = self;
            nself = copy.deepcopy(a);
            for i in range(nself.shape[0]):
                nself.data[i]=nself.data[i]*b;
            return nself;        
    def __rmul__(self, obj):
        tmp = self.ones(self.shape,self.dtype)*obj;
        return tmp/self.__mul__(obj);    
    
    def __truediv__(self, obj):
        # 正向除
        
        if not isinstance(obj,marray) and \
            self.dtype != type(obj):
            raise TypeError('Error data type ',type(obj),' op need marray or ',self.dtype);
        
        if self.dtype == type(obj):
            nself = copy.deepcopy(self);
            if len(nself.shape)>1:
                nself.data=list(map(lambda x:x/obj,nself.data));
            else:
                nself.data=list(map(self.dtype,map(lambda x:x/obj,nself.data)));
            return nself;
        else:
            if self.dtype != obj.dtype:
                raise TypeError('Error data type ',obj.dtype, ' but origin type is ',self.dtype);
            if len(self.shape) == len(obj.shape):
                # 相同时张量阶数时，是各个位置元素相除
                nself = copy.deepcopy(self);
                for i in range(len(self.shape)):
                    if self.shape[i] != obj.shape[i]:
                        raise ValueError('Error data shape ',obj.shape,' but origin shape is ',self.shape);
                    
                if len(nself.shape)>1:
                    nself.data=list(map(lambda x,y:x/y,nself.data,obj.data));
                else:
                    nself.data=list(map(self.dtype,map(lambda x,y:x/y,nself.data,obj.data)));
#                 nself.data=list(map(lambda x,y:x/y,nself.data,obj.data));
                return nself;    
            # 不同阶数时
            elif len(self.shape) > len(obj.shape):
                a = self;
                b = obj;
                nself = copy.deepcopy(a);
                for i in range(nself.shape[0]):
                    nself.data[i]=nself.data[i]/b;
                return nself;
            else:
                a = obj;
                b = self;
                nself = copy.deepcopy(a);
                for i in range(nself.shape[0]):
                    nself.data[i]=b/nself.data[i];
            return nself;

    def __rtruediv__(self, obj):
        return self.__truediv__(obj);    
    
    
    def fill(self,value,shape,dtype):
        data = [dtype(value)]*shape[-1];
        arr  = marray(data,[shape[-1]],dtype);
        for s in shape[-2::-1]:
            tmp=[deepcopy(arr)]*(s-1);
            tmp.append(arr);
            nsp=[s];nsp.extend(arr.shape);
            arr=marray(tmp,nsp,dtype);    
        return arr;
    
    def ones(self,shape,dtype=float):    
        return self.fill(1, shape, dtype);
    
    def zeroes(self,shape,dtype=float):    
        return self.fill(0, shape, dtype);
    
    
    def __str__(self):
        size = self.shape[0];
        if len(self.shape)==1:
            ret='['+str(self.data[0]);
            for i in range(1,size):
                ret+=','+str(self.data[i]);
            ret+=']';
        else:
            ret='[';
            for i in range(0,size-1):
                ret+=str(self.data[i])+'\n';
            ret+=str(self.data[size-1])+']'
        return ret;


if __name__ == '__main__':
    
    a = [1,2,3,4];
    b = [7,8,9,10];
    arr = marray(a,[4],int);
    brr = marray(b,[4],int);
    crr = marray([arr,brr],[2,4],int);
    sarr = arr[0];
    arr[0]=100;
    crr[0]=arr;
    arr[0]=10;
    print(arr);
    print(brr);
#     print(2/crr);
    print(2/crr);
    
    print(-crr[1]);
    print(arr.ones([3,2],float));
#     print(type(arr));
#     
#     print(arr.shape)
#     print(len(arr));
#     arr[3]=9;
#     print(arr);
#     
#     b = [2,9];
#     arr[0:2]=b;
#     print(arr);

    pass