import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
a=[24,25,8,7,12,16,20, 21]
GPIO.setup(a, GPIO.OUT)
#GPIO.setup(21, GPIO.OUT)

def lightUp(ledNumber, period):
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)

def lightdown(ledNumber, period):
    GPIO.output(ledNumber, 0)
    time.sleep(period)

#lightUp(a[0], 2)

def blink(ledNumber, blinkCount, blinkPeriod):
    i=0
    while i < blinkCount:
        lightUp(ledNumber, blinkPeriod)
        lightdown(ledNumber, blinkPeriod)
        i=i+1

#blink(a[0], 2, 1)

def runningLight(count, period):
    i=0
    while i<count:
        j=0
        while j < 8: 
            lightUp(a[j], period)
            GPIO.output(a[j], 0)
            j = j+1
        i=i+1


#runningLight(3, 1)  

def runningDark(count, period):
    i=0
    GPIO.output(a[0], 1)
    GPIO.output(a[1], 1)
    GPIO.output(a[2], 1)
    GPIO.output(a[3], 1)
    GPIO.output(a[4], 1)
    GPIO.output(a[5], 1)
    GPIO.output(a[6], 1)
    GPIO.output(a[7], 1)

    while i<count:
        j=0
        while j < 8: 
            lightdown(a[j], period)
            GPIO.output(a[j], 1)
            j = j+1
        i=i+1

#runningDark(3, 0.5)

def decToBinList(decNumber):
    N = 7
    p = 0
    x = []

    while N>0:
        p = int(decNumber/2**N)
        if p==1:
            x.append(1)
            decNumber -=2**N
        else:
            x.append(0)
        N -= 1
    x.append(decNumber)
    print (x)

decToBinList(1)

GPIO.cleanup()

def lightNumber(number):
    x = decToBinList(number)
    i = 8
    while i > 0:
        if x[i] == 1:
            GPIO.output(a[i], 1)
        i = i-1

lightNumber(235)



