# ThorlabsPM
Thorlabs Power Meter (PM16 and PM100) readout with logging

# Prereqiusities
The script uses ThorlabsPM100 (https://pypi.org/project/ThorlabsPM100/).

The script requires R/W access to the USBTMC device created after the PM is plugged in. For a quick test you can just use chmod:

`sudo chmod 777 /dev/usbtmc2`





The device is preset to /dev/usbtmc2, change this, if needed.

# Usage
`python3 readPower.py`

Press Ctrl-C to stop acquisition.
