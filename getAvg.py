#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:31:51 2020

@author: lada
"""

import numpy as np

filename = "C2test_vlakno2_plny.txt"

file = np.loadtxt(filename, delimiter=" ", dtype='str')
vals = file[:,2].astype('float')
print(np.average(vals))