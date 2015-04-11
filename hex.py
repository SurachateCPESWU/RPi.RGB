#!/usr/bin/evm python
# 11/04/58
# RGB show color from RGB hex
import RPi.GPIO as GPIO
import time

#### Pin led  setup ###
pin_r=11
pin_g=12
pin_b=13
################

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_r,GPIO.OUT)
GPIO.setup(pin_g,GPIO.OUT)
GPIO.setup(pin_b,GPIO.OUT)

r=GPIO.PWM(pin_r,60)
g=GPIO.PWM(pin_g,60)
b=GPIO.PWM(pin_b,60)

r.start(100)
g.start(100)
b.start(100)

def hex_to_per(input):
    r_color= float ("{0:.2f}".format((((int (input[0:2],16))/255)*100)))
    g_color= float ("{0:.2f}".format((((int (input[2:4],16))/255)*100)))
    b_color= float ("{0:.2f}".format((((int (input[4:6],16))/255)*100)))
    show(r,r_color)
    show(g,g_color)
    show(b,b_color)

def show(pin,color):
    dc=100-color
    pin.ChangeDutyCycle(dc)

