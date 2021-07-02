import pandas as pd
import numpy as np

df = pd.Series(range(3), index=['a', 'b', 'c'])
print(f'================df:\n{df}')

# 5.2.1 &&  5.2.2


# 5.2.1 重建索引, Series
# - 如果某个索引值之前并不存在，则会引入缺失值：
# - 如果某个索引值删除了，则对应的value会删除：
df2 = df.reindex(index=['a', 'c', 'd', 'e'])
print("=============df2:\n{}".format(df2))

# 顺序数据的重建索引，会前向填充
obj3 = pd.Series(data=['blue', 'purple', 'yellow'], index=[0, 2, 4])
print("=============obj3:\n{}".format(obj3))

obj4 = obj3.reindex(range(6), method='ffill')
print("=============obj4:\n{}".format(obj4))

# dataframe重建索引
rg = range(9)
arg = np.arange(9)
print("rg:{} type:{}".format(rg, type(rg)))
print("arg:{} type:{}".format(arg, type(arg)))
rarg = np.reshape(arg, (3, 3))
print("rarg:\n{}".format(rarg))

frame = pd.DataFrame(rarg, index=['a', 'c', 'd'], columns=[
                     'Beijing', 'Shanghai', 'Tianjin'])
print("=====================\nframe:{}".format(frame))

# df.reindex
frame1 = frame.reindex(['a', 'b', 'c', 'd'])
print("=====================\nframe.reindex:{}".format(frame1))

# columns reindex
frame2 = frame.reindex(columns=['Beijing', 'Shanghai', 'Hebei'])
print("=====================\nframe.reindex:\n{}".format(frame2))

# 使用loc进行检索 ,许多用户倾向使用loc检索
frame3 = frame.copy()
loc1 = frame3.loc[['a', 'c', 'd'], ['Beijing', 'Shanghai']]
print("=====================\nframe.loc:\n{}".format(loc1))

# drop方法删除行
obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print("=====================\nobj:\n{}".format(obj))

obj_1 = obj.drop('c')
print("=====================\nobj_1:\n{}".format(obj_1))

obj_2 = obj.drop(['c', 'd'])
print("=====================\nobj_2:\n{}".format(obj_2))

# 索引值可以从轴向上删除
cdata  =np.arange(16).reshape(4,4)
states=['Ohio', 'Colorado', 'Utah' ,'New york']
data = pd.DataFrame(cdata, index=states, columns=['one', 'tow', 'three', 'four'])
print("=====================\ndata:\n{}".format(data))

# drop删除行
data_1 = data.drop(['Colorado', 'Ohio'])
print("=====================\ndata:\n{}".format(data_1))

# axis='index' <== axis=0

# drop删除列  axis='columns' <== axis=1
data_2 = data.drop(['tow', 'four'], axis='columns')
print("=====================\ndata:\n{}".format(data_2))

# drop直接删除原对象参数 inplace=True
data3 = data.copy()
data3.drop(['Colorado', 'Ohio'], inplace=True)
print("=====================\ndata:\n{}".format(data3))

data4 = data.copy()
print("=====================\ndata4:\n{}".format(data4))
data4.drop(['tow', 'four'], axis=1, inplace=True) # 从左到右逐列删除
# print("=====================\ndata:\n{}".format(data4))


