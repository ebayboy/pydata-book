
# 5.3.1 相关性和协方差

import pandas as pd
import numpy as np
import pandas_datareader as pdr
import time

#for ticker in ['GS10', 'AAPL', 'IBM', 'MSFT', 'GOOG']:
for ticker in ['GS10']:
    try:
        print("get data: {}...".format(ticker))
        tmp = pdr.get_data_fred(ticker)
        print("tmp:{}".format(tmp))
    except Exception as e:
        print('错误类型是',e.__class__.__name__)
        print('错误明细是',e)

