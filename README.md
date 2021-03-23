# Broken-Phone-Recovery
_a guide how to backup data from your locked android phone if you broke your screen_

_you can skip some steps depending on your situation_ 


You need:
- usb otg adapter for your phone
- usb keyboard
- raspberry pi zero
- a second device to run adb and backup data
- a bluetooth input device (like a joystick controller) or some app to remote control your phone(e.g teamviewer)

## 0. Preparation:
- follow https://github.com/v1nc/Raspberry-Zero-Mouse-Simulation to install mouse simulation on your pi zero
- clone this repo on your pi
- copy `hid-gadget-test` into the repo dir and rename it to `hid`
- turn on sound of your phone if possible, to get some feedback

## 1. Unlock:
### A) Password Lock:
- connect keyboard via otg.
- press ENTER, then SPACE.
- type in your password and hit enter.
- if your password contains y/z and it does not work, your keyboard layout could be different, try switching y/z in your password.
- wait for the click sound to verify its unlocked.

### B) Pattern lock:
- open `unlock.py` in your favorite editor.
- if your pattern does not start in the top left corner, add `move_right()`, `move_left()`, `move_up()` or `move_down()` after line 118, to navigate to your starting point.
- if your pattern is not the small v, edit the lines after 141 to implement your pattern. Look at the examples in the script.
- make sure to copy the modified `unlock.py` to the pi.
- connect the raspberry's otg port to your phone, if your sound does work and you hear the charging sound, remove the cable you connected to your phones otg adapter and reconnect, until you hear a different sound.
- execute `python3 unlock.py`.
- if you get `IOError: [Errno 108] Cannot send after transport endpoint shutdown`, then the raspberry is not connected properly via otg.
- wait for the script to finish and hear the unlock sound, if your sound works.
- if you are lucky and your phone automatically connects to your adb device, you can proceed with step 5.

## 2. Talkback
_the easiest way to control your broken phone is Talkback. Once its enabled, you can use your keyboard to navigate and your phone will read out the screen content_
- if you are lucky and your volume buttons still work, you can enable talkback by holding down vol+ and vol- for 3 seconds.
- keep in mind that to unlock your phone with `unlock.py`, you need to disable talkback again.
- if your volume buttons dont work or the shortcut is disabled, you can use `talkback.py`
- run `python talkback.py`, it will ask you to use google assistant
- using google assistant is more reliable to open apps, but you can also use the mouse emulation to open the settings
- wait for the script to enable talkback


### B) todo: without google assistant

##  3. Prepare adb connection
_if your phone does not automatically enables the adb connection, or you did not authenticate your device with your phone before, you need another input method to enable the connection, because you probably can not connect an usb keyboard and your adb device at the same time._

### A) connect bluetooth controller:
_if you have some bluetooth controller or keyboard, you can use it to control your phone while it should connect to your adb device._

- if you are lucky you already connected the controller and only need to enable bluetooth if disabled.
- otherwise you can use your keyboard and talkback to open settings, enable bluetooth and connect the controller.
- because initial connection is not always straightforward with cheap controllers, you can also use the play store or your favorite app store to install [Screen Stream](https://play.google.com/store/apps/details?id=info.dvkr.screenstream)
- if you are lucky and your phone is connected with your google account, you can login to the playstore on your browser and install the app on your phone without any interaction
- launch the app and navigate with talkback to enable screen sharing. Use TAB to select the button after 'exit' which is probably unnamed, press `ENTER, TAB, TAB, ENTER` to enable the sharing. Then you can watch your screen on `http://phone_ip:8080`.
- next steps will be more comfortable, because you do not need talkback anymore
- finally connect your bluetooth controller/keyboard

### B) connect remote control app:
_if you dont have a bluetooth device, you need to setup a remote control app like teamviewer_

- install [teamviewer host](https://play.google.com/store/apps/details?id=com.teamviewer.host.market) on your phone with talkback, your keyboard and your favorite play store
- if you are lucky and your phone is connected with your google account, you can login to the playstore on your browser and install the app on your phone without any interaction
- install teamviewer on your second device and connect your phone

## 4. Connect adb
- connect your phone to your adb device
- use your bluetooth controller or remote control app to enable developer settings and MTP
- authenticate your device 

## 5. Backup your data
- use other [tutorials](https://gist.github.com/AnatomicJC/e773dd55ae60ab0b2d6dd2351eb977c1) to backup your app data
- some apps like banking or OTP apps set `android:allowBackup=False`, then you can only backup app data if your boot loader is unlocked
- install [scrcpy](https://github.com/Genymobile/scrcpy) to open OTP apps like Aegis and copy your backup code. Most of them disable screen sharing with teamviewer or Screen Stream, but scrcpy works anyway.
