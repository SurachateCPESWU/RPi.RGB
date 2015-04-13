#!/usr/bin/evm python
import RPi.GPIO as GPIO
import time
import lirc

#### Pin led  setup ###
pin_r=11
pin_g=12
pin_b=13
#######################

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

def show(pin,color):
    dc=100-color
    pin.ChangeDutyCycle(dc)

sockid = lirc.init("RPi.RGB")

change_r=0
change_g=0
change_b=0
while 1 :
    a=lirc.nextcode()
    if(a== ['R_UP']):
        change_r+=5
        if((change_r >= 0)and(change_r <= 100)):
            show(r,change_r)
        print("R=%d G=%d B=%d"%(change_r,change_g,change_b))
    elif(a==['R_DOWN']):
        change_r-=5
        if((change_r >= 0)and(change_r <= 100)):
            show(r,change_r)
        print("R=%d G=%d B=%d"%(change_r,change_g,change_b))
    elif(a==['G_UP']):
        change_g+=5
        if((change_g >= 0)and(change_g <= 100)):
            show(g,change_g)
        print("R=%d G=%d B=%d"%(change_r,change_g,change_b))
    elif(a==['G_DOWN']):
        change_g-=5
        if((change_g >= 0)and(change_g <= 100)):
            show(g,change_g)
        print("R=%d G=%d B=%d"%(change_r,change_g,change_b))
    elif(a==['B_UP']):
        change_b+=5
        if((change_b >= 0)and(change_b <= 100)):
            show(b,change_b)
        print("R=%d G=%d B=%d"%(change_r,change_g,change_b))
    elif(a==['B_DOWN']):
        change_b-=5
        if((change_b >= 0)and(change_b <= 100)):
            show(b,change_b)
        print("R=%d G=%d B=%d"%(change_r,change_g,change_b))
    elif(a==['POWER']):
        change_r+=5
        change_g+=5
        change_b+=5
        if((change_r >= 0)and(change_r <= 100)):
            show(r,change_r)
        if((change_g >= 0)and(change_g <= 100)):
            show(g,change_g)
        if((change_b >= 0)and(change_b <= 100)):
            show(b,change_b)
        print("R=%d G=%d B=%d"%(change_r,change_g,change_b))
    elif(a==['POWER2']):
        change_r-=5
        change_g-=5
        change_b-=5
        if((change_r >= 0)and(change_r <= 100)):
            show(r,change_r)
        if((change_g >= 0)and(change_g <= 100)):
            show(g,change_g)
        if((change_b >= 0)and(change_b <= 100)):
            show(b,change_b)
        print("R=%d G=%d B=%d"%(change_r,change_g,change_b))
    elif(a==['key_7']):
        change_r=0
        change_g=0
        change_b=0
        for change_r in range(0,100,2):
            show(r,change_r)
            time.sleep(0.1)
        for change_b in range(0,100,2):
            show(b,change_b)
            time.sleep(0.1)
        for change_r in range(100,0,-2):
            show(r,change_r)
            time.sleep(0.1)
        for change_g in range(0,100,2):
            show(g,change_g)
            time.sleep(0.1)
        for change_b in range(100,0,-2):
            show(b,change_b)
            time.sleep(0.1)
        for change_r in range(0,100,2):
            show(r,change_r)
            time.sleep(0.1)
        for change_g in range(100,0,-2):
            show(g,change_g)
            time.sleep(0.1)
        for change_r in range(100,0,-2):
            show(r,change_r)
            time.sleep(0.1)
