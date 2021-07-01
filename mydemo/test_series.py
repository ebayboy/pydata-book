import pandas as pd

# 1. 使用list生成Series
idx = ['a', 'b', 'c', 'd', 'e']
vTMW = [101, 102, 103, 104, 105]
obj_0 = pd.Series(vTMW)
print("obj_0.index:{}".format(obj_0.index))
print("obj_0.count:{}".format(obj_0.count()))

print("=============================")
obj = pd.Series(vTMW, idx)

print("obj:{}".format(obj))

print('d:{}'.format(obj[3]))

# by tital
print('d:{}'.format(obj['d']))

# iloc <==> obj[3]
print('iloc:{}'.format(obj.iloc[3]))

# loc <==> obj['c']
print('loc:{}'.format(obj.loc[['c', 'e']]))

# loc 2
print('loc:{}'.format(obj.loc['c':'e']))


# 2. 使用字典生成Seris
print("===============================")
names = ['fanpf', 'rose', 'fanyx']
sdata = {'rose': 32, 'fanpf': 33, 'fanyx': 8}
obj2 = pd.Series(sdata, index=names)
print("obj2:{}".format(obj2))
print("obj2.index:{}".format(obj2.index))

# 2.2
print("================================")
names_3 = ['luoluo', 'fanpf', 'rose', 'fanyx']
obj3 = pd.Series(sdata, index=names_3)
print(f"obj3:{obj3}")
print("obj3:{}".format(pd.isnull(obj3)))

print("luouo:{}".format(obj3.loc['luoluo']))
luoluo = obj3.loc['luoluo']
if pd.isnull(luoluo):
    print("isnull")
else:
    print("notnull")


