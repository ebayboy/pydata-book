import numpy as np
import pandas as pd

# 5.2.3 索引、选择与过滤

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print("obj:\n{}".format(obj))

# 索引格式： ['b'] , [2:4], [1], ['a', 'b', 'c'] , [[1,3]]

print(f"{obj[1]}")
print(f"{obj[1:3]}")
print("{}".format(obj[['a','c']]))
print("{}".format(obj[[1, 3]]))
print("{}".format(obj[ obj < 2 ]))

# 通过标签连续索引
# Series的索引是包含尾部'c'元素的
print(f"===========b:c \n{obj['b']}")

# 普通的切片不包含尾部
l = np.arange(5)
print("l:{}".format(l[2:3]))

print("=============obj:\n{}".format(obj))

# set obj['b':'c'] , obj[['b', 'c', 'd']]
obj1 = obj.copy()
obj1['b':'c'] = 5
print("=============obj:\n{}".format(obj1))

obj2 = obj.copy()
obj2[['b', 'd']] = 5
print("=============obj:\n{}".format(obj2))

# 从DataFrame中索引出一个或多个列
data = pd.DataFrame(np.arange(16).reshape(4,4), index=['Ohio', 'Colorado', 'Utah', 'New york'], 
        columns=['one', 'tow', 'three', 'four'])
print("=============data:\n{}".format(data))

print("=============data['tow']:\n{}".format(data['tow']))
print("=============data.loc['Utah']:\n{}".format(data.loc['Utah', ['one', 'three']]))

print("=============data:\n{}".format(data[:2]))

# 检索three列 > 5的行
print("=============data:\n{}".format(data[data['three'] > 5]))

# 检索 data元素 < 5的元素
print("=============data:\n{}".format(data < 5))







