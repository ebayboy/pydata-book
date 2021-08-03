import numpy as np

# reversed/zip函数使用后的对象都需要用list转一下
lst = np.arange(1, 10)
lst_reversed = list(reversed(lst))
print("lst_reversed:{}".format(lst_reversed))

