import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

# Modules for my apps
import nomics

PORT_BUZZER = 2             # D2
PORT_RED_BUTTON = 3         # D3
PORT_GREEN_BUTTON = 4       # D4

LCD_LINE_LEN = 16

# Connect the Grove Rotary Angle Sensor to analog port A0
# SIG,NC,VCC,GND
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# Setup
grovepi.pinMode(PORT_BUZZER, "OUTPUT")
grovepi.pinMode(PORT_GREEN_BUTTON, "INPUT")
grovepi.pinMode(PORT_RED_BUTTON, "INPUT")

lcd.setRGB(0, 128, 0)

# Installed Apps!
APPS = [
    nomics.BITCOIN_APP
]

while True:
    try:
        temp = APPS
        # Display app name
        lcd.setText_norefresh(APPS[app]['name'])

    except KeyboardInterrupt:
        # Gracefully shutdown on Ctrl-C
        lcd.setText('')
        lcd.setRGB(0, 0, 0)

        # Turn buzzer off just in case
        grovepi.digitalWrite(PORT_BUZZER, 0)

        break

    except IOError as ioe:
        if str(ioe) == '121':
            # Retry after LCD error
            time.sleep(0.25)

        else:
            raise
