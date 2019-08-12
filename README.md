# ThorlabsPM
Thorlabs Power Meter (PM16 and PM100) readout with logging

# Prereqiusities
The script uses ThorlabsPM100 (https://pypi.org/project/ThorlabsPM100/).

The script requires R/W access to the USBTMC device created after the PM is plugged in. For a quick test you can just use chmod:

`sudo chmod 666 /dev/usbtmc2`

Permanent solution can be creating the file /etc/udev/rules.d/99-ThorlabsPM.rules with the following content:
```
SUBSYSTEMS=="usb", DRIVERS=="usbtmc", MODE="0666"
```

The device is preset to /dev/usbtmc2, change this, if needed.

# Usage
`python3 readPower.py`

Press Ctrl-C to stop acquisition.
