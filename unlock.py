#!/usr/bin/env python3
import time, os

N = chr(0)
CLICK_LEFT=chr(1)+N*3
ENTER=40
SPACE=44

def raw_mouse(key):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(key.encode())

def raw_keyboard(key):
	with open('/dev/hidg1', 'rb+') as fd:
		fd.write(key.encode())

def press_and_release(key):
	raw_keyboard(key)
	raw_keyboard(N*8)

def move_mouse(x,y):
	os.system("echo ' {} {}' | ./hid /dev/hidg0 mouse > /dev/null".format(x,y))
	time.sleep(0.1)

def move_mouse_hold(x,y):
	os.system("echo '--hold --b1 {} {}' | ./hid /dev/hidg0 mouse > /dev/null".format(x,y))
	time.sleep(0.1)

def type_key(key):
	press_and_release(N*2+chr(key)+N*4)
	time.sleep(1)

def down_right():
	move_mouse_hold(100,100)
	move_mouse_hold(100,100)
	move_mouse_hold(70,62)

def up_right():
	move_mouse_hold(100,-100)
	move_mouse_hold(100,-100)
	move_mouse_hold(70,-62)

def down_left():
	move_mouse_hold(-100,100)
	move_mouse_hold(-100,100)
	move_mouse_hold(-70,62)	

def up_left():
	move_mouse_hold(-100,-100)
	move_mouse_hold(-100,-100)
	move_mouse_hold(-70,-62)

def down():
	move_mouse_hold(0,100)
	move_mouse_hold(0,100)
	move_mouse_hold(0,70)

def up():
	move_mouse_hold(0,-100)
	move_mouse_hold(0,-100)
	move_mouse_hold(0,-70)

def left():
	move_mouse_hold(-100,0)
	move_mouse_hold(-100,0)
	move_mouse_hold(-70,0)

def right():
	move_mouse_hold(100,0)
	move_mouse_hold(100,0)
	move_mouse_hold(70,0)

def move_down():
	move_mouse(0,100)
	move_mouse(0,100)
	move_mouse(0,70)

def move_up():
	move_mouse(0,-100)
	move_mouse(0,-100)
	move_mouse(0,-70)

def move_left():
	move_mouse(-100,0)
	move_mouse(-100,0)
	move_mouse(-70,0)

def move_right():
	move_mouse(100,0)
	move_mouse(100,0)
	move_mouse(70,0)

# turn on screen(this does not work on some phones, you can remove the line and turn on screen with the power button)
type_key(ENTER)
# open pattern screen
type_key(SPACE)
# reset mouse
raw_mouse(4*N)

# move cursor to the top left corner of the screen 
for i in range(30):
	move_mouse(-100,-100)

# move cursor to the y position of the top left pattern point 
# 12 works good for >6 inch, 11 for <6 inch
for i in range(12):
	move_mouse(0,100)

# move cursor over the top left pattern point
move_right()

# add move_* here to change your starting point
# example: bottom right corner:
#move_right()
#move_right()
#move_down()
#move_down() 

# start the click
raw_mouse(CLICK_LEFT)

# draw your pattern

# example: L
#down()
#down()
#right()
#right()

# example: O
#down()
#down()
#right()
#right()
#up()
#up()
#left()
#left()

# example: v
down_right()
up_right()

# stop the click
raw_mouse(4*N)
