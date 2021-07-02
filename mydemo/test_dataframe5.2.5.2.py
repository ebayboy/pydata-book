
# 5.2.5.2 DataFrame和Series间的操作
import numpy as np
import pandas as pd

# numpy 数组操作

'''
=======frame:
             c0    c1    c2
         r0  0.0   1.0   2.0
         r1  3.0   4.0   5.0
         r2  6.0   7.0   8.0
         r3  9.0  10.0  11.0
'''
arr = np.arange(12.).reshape((3,4))
print("=======arr:\n{}".format(arr))

print("=======arr:\n{}".format(arr[0]))
print("=======arr:\n{}".format(arr - arr[0]))

# dataframe和series操作
frame = pd.DataFrame(np.arange(12.).reshape((4,3)), index=['r0', 'r1', 'r2', 'r3'],
        columns=['c0', 'c1', 'c2'])
print("=======frame:\n{}".format(frame))

# ser1: r0  0.0   1.0   2.0
ser1 = frame.iloc[0, :] # 选择第一行
print("=======ser1:\n{}".format(ser1))
# 行相加
frame1 = frame.add(ser1, axis='columns') # 行相加, 从左到右逐个元素进行add操作
print("=======frame1:\n{}".format(frame1))

ser2 = frame.iloc[:, 0] # 选择第一列
print("=======ser2:\n{}".format(ser2))
# 列相加
frame2 = frame.add(ser2, axis='index') #  axis = 0, 从上到下相加, 逐个元素进行add操作
print("=======frame2:\n{}".format(frame2))



