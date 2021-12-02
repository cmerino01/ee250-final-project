import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

# Modules for my apps
import nomics

PORT_BUZZER = 2             # D2
PORT_BUTTON = 8             # D8
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

lcd.setRGB(255, 255, 255)

# Installed Apps!
APPS = [
    nomics.BITCOIN_APP
]

# Cache to store values so we save time and don't abuse the APIs
CACHE = [''] * len(APPS)
for i in range(len(APPS)):
    # Includes a two space offset so that the scrolling works better
    CACHE[i] = '  ' + APPS[i]['init']()

app = 0     # Active app
ind = 0     # Output index

init_price = float(CACHE[app][ind:ind+LCD_LINE_LEN])
init_price = round(init_price, 2)

while True:
    try:

        if grovepi.digitalRead(PORT_BUTTON):
            #make a new call to API to get updated price
            APPS = [ nomics.BITCOIN_APP ] 
            # Cache to store values so we save time and don't abuse the APIs
            CACHE = [''] * len(APPS)
            for i in range(len(APPS)):
                # Includes a two space offset so that the scrolling works better
                CACHE[i] = '  ' + APPS[i]['init']()
            updated_price = float(CACHE[app][ind:ind+LCD_LINE_LEN])
            updated_price = round(updated_price, 2)

            #hit the lights
            if(updated_price == init_price):
                grovepi.digitalWrite(PORT_GREEN_BUTTON, 1)
                grovepi.digitalWrite(PORT_BUZZER, 1)
                time.sleep(1)
                grovepi.digitalWrite(PORT_BUZZER, 0)
                grovepi.digitalWrite(PORT_GREEN_BUTTON, 0)
            elif(updated_price > init_price):
                init_price = updated_price
                grovepi.digitalWrite(PORT_GREEN_BUTTON, 1)
                grovepi.digitalWrite(PORT_BUZZER, 1)
                #recovery period (meant to prevent overloading api requests)
                time.sleep(1)
                grovepi.digitalWrite(PORT_BUZZER, 0)
                grovepi.digitalWrite(PORT_GREEN_BUTTON, 0)
            elif(updated_price < init_price):
                init_price = updated_price
                grovepi.digitalWrite(PORT_RED_BUTTON, 1)
                grovepi.digitalWrite(PORT_BUZZER, 1)
                #recovery period (meant to prevent overloading api requests)
                time.sleep(1)
                grovepi.digitalWrite(PORT_BUZZER, 0)
                grovepi.digitalWrite(PORT_RED_BUTTON, 0)

        #lcd.setText_norefresh(APPS[app]['name'])    # Display app name
        lcd.setText_norefresh(APPS[app]['name'] + '\n' + '$' + str(init_price))  #Display Output

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
