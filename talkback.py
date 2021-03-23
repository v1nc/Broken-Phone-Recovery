#!/usr/bin/env python3
import time, os

N = chr(0)
A=4
B=5
C=6
K=14
L=15
T=23
NN=17


ENTER=40
TAB=43
WINDOWS=8

def raw_keyboard(key):
	with open('/dev/hidg1', 'rb+') as fd:
		fd.write(key.encode())

def multi_press(keys):
	for key in keys:
		press(key)

def press(key):
	raw_keyboard(N*2+chr(key)+N*5)
	raw_keyboard(N*8)
	time.sleep(1)

def press_with_mod(key,mod):
	raw_keyboard(chr(mod)+N+chr(key)+N*5)
	raw_keyboard(N*8)
	time.sleep(1)

def move_mouse(x,y):
	os.system("echo ' {} {}' | ./hid /dev/hidg0 mouse > /dev/null".format(x,y))
	time.sleep(0.1)

def click():
	os.system("echo '--b1' | ./hid /dev/hidg0 mouse > /dev/null")
	time.sleep(0.1)

if input("Use google assistant to open settings? (Y/n): ").lower() == "n":
	press_with_mod(NN,WINDOWS)
	for i in range(30):
		move_mouse(100,-100)
	move_mouse(-80,100)
	move_mouse(0,60)
	time.sleep(1)
	click()

else:
	print("say 'open settings' in your device language")
	time.sleep(0.5)
	press_with_mod(0,WINDOWS)

time.sleep(10)
press(ENTER)
multi_press([T,A,L,K,B,A,C,K])
for i in range(4):
	press(ENTER)
press(TAB)
press(TAB)

press(ENTER)
