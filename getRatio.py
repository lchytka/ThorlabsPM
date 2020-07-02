#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:31:51 2020

@author: lada
"""

import numpy as np

filename1 = "C2test_vlakno1_podstred_3.txt"
filename2 = "C2test_vlakno2_podstred_3.txt"

file1 = np.loadtxt(filename1, delimiter=" ", dtype='str')
file2 = np.loadtxt(filename2, delimiter=" ", dtype='str')
vals1 = file1[:,2].astype('float')
vals2 = file2[:,2].astype('float')
print(np.average(vals1)/np.average(vals2))