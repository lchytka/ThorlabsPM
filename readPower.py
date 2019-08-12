#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 09:25:32 2019

@author: lada
"""

from ThorlabsPM100 import ThorlabsPM100, USBTMC
import matplotlib.pyplot as plt
from time import sleep
from datetime import datetime

# PM init -- needs RW rights set for the device
inst = USBTMC(device="/dev/usbtmc2")
power_meter = ThorlabsPM100(inst=inst)
power_meter.sense.correction.wavelength = 400

filename = datetime.utcnow().strftime("power_%Y%m%d_%H%M.csv")
with open(filename,"a") as file:
    file.write("# Thorlabs Power Meter measurement log\n")
    file.write("# Preset wavelength: "+str(power_meter.sense.correction.wavelength))
    file.write("\n######################################\n")
    file.write("# Date and time,\tPM value [W]\n")

i=0
while(True): 
    time = datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")
    meas = power_meter.read
    with open(filename,"a") as file:
        file.write(time+",\t"+str(meas)+"\n")
    print(time+": "+str(meas))
    sleep(1)
    

