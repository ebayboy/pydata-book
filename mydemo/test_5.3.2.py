
import pandas as pd
import numpy as np


obj = pd.Series(list('cadaabbc'))

print("========obj:\n{}".format(obj))

# obj.unique()
print("========obj.unique:\n{}".format(obj.unique()))

# sort
uniques = obj.unique()
print("========obj.uniques:\n{}".format(uniques))

mask = obj.isin(list('bc'))
print("========mask:\n{}".format(mask))

# 过滤子集
print("========obj[mask]:\n{}".format(obj[mask]))

# index
to_match = pd.Series(list('cabbca'))
unique_vals = pd.Series(list('cba'))
idxs1 = pd.Index(unique_vals)
print("========idxs_1:\n{}".format(idxs1)) # [0 2 1 1 0 2] 

idxs = pd.Index(unique_vals).get_indexer(to_match)
print("========idxs:\n{}".format(idxs)) # [0 2 1 1 0 2] 

# 计算多列直方图
data = pd.DataFrame({'Qu1':[1, 3, 4, 3, 4], 'Qu2':[2, 3, 1, 2, 3], 'Qu3':[1, 5 ,2, 4, 4]})
print("data:{}".format(data))
result = data.apply(pd.value_counts).fillna(0)
print("result:{}".format(result))

