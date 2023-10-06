# Imports go at the top
from microbit import *
import netbit
import time

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

node = None

if controller:
    node = netbit.NetController()
else:
    node = netbit.NetNeuron()

time.sleep(2)

node.rollcall()

time.sleep(100)

