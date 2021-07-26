#!/usr/bin/python

import numpy as np
import pandas as pd

ser = pd.Series(np.arange(0, 5), index=list('abcde'))

print("ser:\n{}".format(ser))

del ser['b']
print("ser:\n{}".format(ser))


