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
    my_weather.WEATHER_APP,
    my_reddit.QOTD_APP,
    # TODO: Add your new app here
    my_anime.ANIME_APP
]

# Cache to store values so we save time and don't abuse the APIs
CACHE = [''] * len(APPS)
for i in range(len(APPS)):
    # Includes a two space offset so that the scrolling works better
    CACHE[i] = '  ' + APPS[i]['init']()

app = 0     # Active app
ind = 0     # Output index

ogthresh = -1
while True:
    try:
        threshold = int(grovepi.analogRead(potentiometer))
        conv = threshold / 1023
        threshold = conv * 4
        threshold = int(threshold)
        print(threshold)
        time.sleep(0.1)

        # Check for input
        if(ogthresh == threshold):
            pass
        elif(ogthresh != threshold):
            ogthresh = threshold
            if(threshold == 0):
                lcd.setRGB(0,0,0)
            elif(threshold == 1):
                lcd.setRGB(255,0,0)
            elif(threshold == 2):
                lcd.setRGB(0,255,0)
            elif(threshold == 3):
                lcd.setRGB(255,223,0)
            elif(threshold == 4):
                lcd.setRGB(0,128,128)


        if grovepi.digitalRead(PORT_GREEN_BUTTON):
            # BEEP!
            grovepi.digitalWrite(PORT_BUZZER, 1)

            # Switch app
            app = (app + 1) % len(APPS)
            ind = 0

        time.sleep(0.1)

        grovepi.digitalWrite(PORT_BUZZER, 0)

        # Display app name
        lcd.setText_norefresh(APPS[app]['name'])

        # Scroll output
        lcd.setText_norefresh('\n' + CACHE[app][ind:ind+LCD_LINE_LEN])
        # TODO: Make the output scroll across the screen (should take 1-2 lines of code)
        ind += 1
        if (ind >= len(CACHE[app])):
            ind -= len(CACHE[app])
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
