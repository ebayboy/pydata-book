
import pandas as pd
import numpy as np

# 5.2.7 排序和排名

# Series
ser = pd.Series(np.random.random_integers(1,100, size=4), index=['r1', 'r2', 'r0', 'r3'])
print("=====ser:\n{}".format(ser))

# Series.sort_index
ser1 = ser.sort_index()
print("=====ser:\n{}".format(ser1))


# dataframe
frame = pd.DataFrame(np.random.random_integers(1,100, size=12).reshape(4,3), index=list('dacb'), columns=list('yxz'))
print("=====frame:\n{}".format(frame))

frame1 = frame.sort_index() # 默认axis = 0, 从上到下操作， 按照index排序
print("=====frame axis=0:\n{}".format(frame1))

frame11 = frame.sort_index(ascending = False) # 默认axis = 0, 从上到下操作， 按照index排序, asc = false, 降序
print("=====frame axis=0 ascending = Flase:\n{}".format(frame11))

frame2 = frame.sort_index(axis=1) # 按列排序
print("=====frame axis=1:\n{}".format(frame2))

ser2 = ser.copy()
print("=====obj:\n{}".format(ser2))
print("=====obj:\n{}".format(ser2.sort_values()))

frame3 = pd.DataFrame({'b':[4,7,-3,2], 'a':[0,1,0,1]})
print("=====fr_s:\n{}".format(frame3))
# frame sort by values a,b
print("=====frame_sort_values:\n{}".format(frame3.sort_values(by=['a','b'])))


# 排名： rank
obj = pd.Series([7, -5, 7, 4 ,2, 0 , 4])
print("=====obj:\n{}".format(obj))
print("=====obj:\n{}".format(obj.rank()))
print("=====obj:\n{}".format(obj.rank(method='first')))


print("=====obj:\n{}".format(frame))
print("=====obj:\n{}".format(frame.rank(ascending=False)))
print("=====obj:\n{}".format(frame.rank(ascending=False, axis=1)))





