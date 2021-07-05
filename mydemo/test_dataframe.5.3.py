
# 5.3 描述性统计的概述与计算

import pandas as pd
import numpy as np

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=list('abcd'), columns=['one', 'tow'])
print("========== df:\n{}".format(df))

print("========== df:\n{}".format(df.sum()))
print("========== df:\n{}".format(df.sum(axis=1))) # 从左向右计算， 将一行的各个列都相加
print("========== df:\n{}".format(df.sum(axis=1, skipna=False))) # skipna : 是否排除Na列

print("========== df.idxmax:\n{}".format(df.idxmax()))
print("========== df.idxmin:\n{}".format(df.idxmin()))

# 积累方法
print("========== df:\n{}".format(df))
print("========== df.cumsum():\n{}".format(df.cumsum()))

# descripbe
print("========== df.describe():\n{}".format(df.describe()))


# secries.describe

ser = pd.Series(list('aabc')*4)
print("===========ser:\n{}".format(ser))
print("===========ser.describe():\n{}".format(ser.describe()))

