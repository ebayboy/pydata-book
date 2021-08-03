
import numpy as np


# build-in func enumerate
lst = np.arange(1, 10)
for i, v in enumerate(lst):
    print(f" i:{i} v:{v}")

some_list = ['foo', 'bar', 'baz']
mapping = {}

for i, v in enumerate(some_list):
    mapping[i] = v

print(f"mapping:{mapping}")



