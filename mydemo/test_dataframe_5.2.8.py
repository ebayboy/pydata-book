
# 5.2.8 含有重复标签的轴索引

import pandas as pd 
import numpy as np

# 1. Series
obj = pd.Series(np.arange(0,5), index=list('aabbc'))
print("=========obj:\n{}".format(obj))

# is_unique
print("=========obj:\n{}".format(obj.index.is_unique))

# 重复索引，返回序列
print("=========obj:\n{}".format(obj['a']))


# 2. DataFrame 重复索引dataframe
df = pd.DataFrame(np.random.randn(4,3), index=list('aabb'))
print("=========df:\n{}".format(df))

print("=========obj:\n{}".format(obj.index.is_unique))

print("=========obj:\n{}".format(obj.loc['b']))

