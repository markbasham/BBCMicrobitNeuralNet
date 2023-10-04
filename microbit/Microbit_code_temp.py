# Imports go at the top
from microbit import *
import netbit as nb
import time
import radio

display.show('')
timeout = 10
time_count = 0
controller = False

while time_count < timeout :
    display.show(time_count)
    if button_a.was_pressed():
        display.show('?')
        controller = True
        time_count = timeout+1
    time_count += 1
    time.sleep(1)

if controller:
    display.show(Image.PACMAN)
else:
    display.show(Image.GHOST)

time.sleep(10)

time_count = 0
while time_count < 2:
    display.scroll('SN:')
    display.scroll(nb.get_serial_number())
    print(nb.get_serial_number()
    time_count += 1


radio.config(group=23)
radio.on()

time_count = 0

name_list = ['go']

if controller:
    while time_count < 2:
        display.show(time_count)
        radio.send('rollcall')#+':'.join(name_list))
        reply_time = 0
        time.sleep_ms(400)
        reply_time = 400
        while reply_time < 1000:
            message = radio.receive()
            if message != '':
                name_list.append(message)
            time.sleep_ms(10)
            reply_time += 10
else:
    display.show(Image.GHOST)
    while True:
        message = radio.receive()
        if message == 'rollcall':
            display.show(Image.HAPPY)
            time.sleep_ms(500)
            radio.send(nb.get_serial_number())

