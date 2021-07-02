
import numpy as np
import pandas as pd


# 5.2.3.1 使用loc && iloc选择数据, ix方法已经弃用

obj = pd.DataFrame(np.arange(16).reshape(4,4), index=['Beijing', 'Shanghai', 'Tianjin', 'Hebei'],
        columns=['one', 'tow', 'three', 'four'])
print("==========obj:\n{}".format(obj))

# 使用iloc选择
print("==========obj:\n{}".format(obj.iloc[2, [3, 0, 1]]))
print("==========obj:\n{}".format(obj.iloc[[0,1], [3, 0, 1]]))
print("==========obj:\n{}".format(obj.iloc[1:2, [3, 0, 1]]))

# 使用loc选择
# 使用标签
print("==========obj:\n{}".format(obj.loc['Beijing', ['tow', 'three']]))

# 使用标签范围
print("==========obj:\n{}".format(obj.loc[:'Tianjin', ['tow', 'three']]))

# 标签范围 + 过滤
print("==========obj:\n{}".format(obj.loc[:'Tianjin', ['tow', 'three']][obj.three > 5]))
print("==========obj:\n{}".format(obj.iloc[:, :3][obj.three > 5]))

# loc & iloc
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print("=============ser2:\n{}".format(ser2))
print("=============ser2[-1]:\n{}".format(ser2[-1])) #使用整数索引
print("=============ser2.iloc[:1]:\n{}".format(ser2.iloc[:1])) #iloc索引
print("=============ser2.loc[:1]:\n{}".format(ser2.loc['a':'c'])) #loc索引

ser3 = pd.Series(np.arange(3.))
print("=============ser3:\n{}".format(ser3))
print("=============ser3.loc[:1]:\n{}".format(ser3.loc[:1])) 
print("=============ser3.iloc[:1]:\n{}".format(ser3.iloc[:1])) 

# Series相加： series1 +series2
ser1 = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])
ser2 = pd.Series(np.arange(5), index=['a', 'c', 'd', 'f', 'g'])
print("=========ser1:\n{}".format(ser1))
print("=========ser2:\n{}".format(ser2))

ser3 = ser1 + ser2
print("=========ser3:\n{}".format(ser3))


# dataframe相加, 相交的部分才进行运算， 否则为NaN
df1 = pd.DataFrame(np.arange(start=0, stop=16, step=1).reshape(4,4), index=['r0', 'r1', 'r2', 'r3'], columns=['c0', 'c1', 'c2', 'c3'])
df1_cp = df1.copy()
print("=========df1:\n{}".format(df1))
df2 = pd.DataFrame(np.arange(start=0, stop=32,step=2).reshape(4,4), index=['r0', 'r2', 'r3', 'r4'], columns=['c0', 'c2', 'c3', 'c4'])
print("=========df2:\n{}".format(df2))

df3 = df1 + df2
print("=========df3:\n{}".format(df3))

# 使用0填充确实的r4和c4
df1.loc[:, 'c4'] = 0
df1.loc['r4', :] = 0

print("=========df1:\n{}".format(df1))
df4 = df1.add(df2, fill_value=0)
print("=========df4 fill_value=0:\n{}".format(df4))

# 使用/进行翻转
df5 = df1_cp.copy()
print("=========df5:\n{}".format(df5))
print("=========1 / df5:\n{}".format(1 / df5))







