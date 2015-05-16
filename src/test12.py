#-*- coding: utf-8 -*-
'''
Created on 2015年3月27日

@author: linglong
'''

import numpy as np
import talib

close = numpy.random.random(100)
output = talib.SMA(close)

from talib import MA_Type
upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)


a = np.arange(6).reshape(2,3)
a.item(1,2)
type(a.item)
