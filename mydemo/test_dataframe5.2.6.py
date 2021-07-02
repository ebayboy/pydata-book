import pandas as pd
import numpy as np


# 5.2.6 函数应用和映射

obj = pd.DataFrame(np.random.randn(4,3), index=['r0', 'r1', 'r2', 'r3'], columns=['c0', 'c1', 'c2'])
print("=====obj:\n{}".format(obj))

f = lambda x : x.max() - x.min()

# 列运算
obj1 = obj.apply(f, axis=0) # 从上向下 计算
print("=====obj axis=0:\n{}".format(obj1))

# 行运算
obj2 = obj.apply(f, axis=1) # 从左到右 计算
print("=====obj axis=1:\n{}".format(obj2))

#apply 返回series
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])

# axis=1 从左到右计算，返回的是行
# axis=0 从上到下计算，返回的是列
obj3 = obj.apply(f, axis=1)
print("=====obj axis=1:\n{}".format(obj3))

fmt = lambda x: '%.2f' % x
a = 3.1415926
b = fmt(a)
print("b:{}".format(b))

# applymap(func) : 逐个元素应用计算函数
obj4 = obj.applymap(fmt)
print("=====obj4:\n{}".format(obj4))





