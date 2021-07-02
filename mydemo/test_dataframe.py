
import pandas as pd

# create df use dict, key == col-key , value == col-value
data = {'state': ['Beijing', 'Shanghai', 'HeBei', 'ShanDong'],
        'year': [2001, 2002, 2003, 2004],
        'pop': [1.5, 1.7, 3.6, 2.4]}

df1 = pd.DataFrame(data)
print("df1:{}".format(df1))

print("head:\n{}".format(df1.head()))
print("tail:\n{}".format(df1.tail()))

# 指定列的顺序
df2 = pd.DataFrame(data, columns=['year', 'pop', 'state'])
print("==============\ndf2:\n{}".format(df2))

# 列不存在
df3 = pd.DataFrame(data, columns=['year', 'state', 'size'])
print("=============\ndf3:\n{}".format(df3))
print("isnull:{}".format(pd.isnull(df3)))


# 指定列的顺序, with index
idxs = ['one', 'tow', 'tree', 'four']
df4 = pd.DataFrame(data, columns=['state', 'pop', 'year'], index=idxs)
print("===============\ndf4_with_index:\n{}".format(df4))

print("df4.columns:{}".format(df4.columns))

# 获取行: 使用loc && iloc获取行，
# 获取列: 使用[index] && ['table']

# 获取dataframe中一行
print("df4.loc['one']:{}".format(df4.loc['one']))

# 获取dataframe中的一列
print("df4.['state']:{}".format(df4['state']))

# 修改一列的值
df4['state'] = 'new-state'
print("df4.['state']:{}".format(df4['state']))

# 修改一行的值
df4.loc['one'] = 'new-row'
print("df4.loc['one']:{}".format(df4.loc['one']))

# 1.1 修改矩阵中某个元素[x,y]的值
df4.loc['tow']['state'] = 'state-xxxx'
print("df4:{}".format(df4))

# 1.2 修改矩阵中某个元素[x,y]的值
df4['state'].loc['one'] = 'state-yyyy'
print("df4:{}".format(df4))


# add new-col(Series) to DataFrame
df5 = pd.DataFrame(data, index=['one', 'tow', 'tree', 'four'])
print('df5:{}'.format(df5))

s1 = pd.Series([1, 2, 3], index=['one', 'tow', 'tree'])
print("s1:{}".format(s1))
df5['new col'] = s1
print("df5:{}".format(df5))

# del col
del df5['new col']
print("del df5['new col']:{}".format(df5))

# TODO: add new row to DataFrame: dataframe是按列组织数据的，
# 每一列是一个series， 添加一行相当于给每一列（series）添加一个新元素

# dataframe - 字典嵌套
# 如果嵌套字典被赋值给DataFrame, pandas会将字典的键作为列，将内部字典的键作为行索引：
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
df6 = pd.DataFrame(pop)
print(f"===================\ndf6:\n{df6}")

# 行列转换
print(f"===================\ndf6.T\n:{df6.T}")

# 如果已经显式指明索引的话，内部字典的键将不会被排序：
df7 = df6.copy()
df7.index = [11, 22, 33]
print(f"===================\ndf7:\n{df7}")

# 使用包含series的字典构造dataframe
print("df6:{}".format(df6))
series1 = df6['Ohio'][:-1]  # -1: 倒数第二个
series2 = df6['Nevada'][:2]  
print("====================\nseries1:{}".format(series1))
print("====================\nseries2:{}".format(series2))

pdata = { 'Ohio' : series1, 'Nevada': series2 }
df8 = pd.DataFrame(pdata)
df8.index.name = 'year'
df8.columns.name = 'state'
print("====================\ndf8:\n{}".format(df8))
print("====================\ndf8.values:\n{}".format(df8.values))

# dtypes 如果DataFrame的列是不同的dtypes，则values的dtype会自动选择适合所有列的类型：
print("====================\n df1.dtypes:{}\n===== df8.dtypes:{}".format(df1.dtypes, df8.dtypes))




