# Broken-Phone-Recovery
_a guide how to backup data from your locked android phone if you broke your screen_

_you can skip some steps depending on your situation_ 


You need:
- usb otg adapter for your phone
- usb keyboard
- raspberry pi zero
- a second device to run adb and backup data

## 0. Preparation:
- follow https://github.com/v1nc/Raspberry-Zero-Mouse-Simulation to install mouse simulation on your pi zero
- clone repo on your pi
- copy `hid-gadget-test` into the repo dir and rename it `hid`
- turn on sound of your phone if possible, to get some feedback

## 1. Unlock:
A) Password Lock:
- connect keyboard via otg
- press ENTER, then SPACE
- type in your password and hit enter
- if your password contains y/z and it does not work, your keyboard layout could be different, try to switch them.
- wait for the click sound to verify its unlocked

B) Pattern lock:
- open `unlock.py` in your favorite editor
- if your pattern does not start in the top left corner, add `move_right()`, `move_left()`, `move_up()` or `move_down()` after line 118, to navigate to your starting point
- if your pattern is not the small v, edit the lines after 141 to implement your pattern.
- make sure to copy the modified `unlock.py` to the pi
- connect the raspberrys otg port to your phone, if your sound does work and you hear the charging sound, remove the cable you connected to your phones otg adapter and reconnect, until you hear a different sound
- execute `python3 unlock.py`
- if you get `IOError: [Errno 108] Cannot send after transport endpoint shutdown`, then the raspberry is not connected properly. 
- wait for the script to finish and hear the unlock sound, if your sound works
