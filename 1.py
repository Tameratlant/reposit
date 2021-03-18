import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
a=[24,25,8,7,12,16,20, 21]
GPIO.setup(a, GPIO.OUT)


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
    return (x)



def lightNumber(number):

    GPIO.output(a[0], 0)
    GPIO.output(a[1], 0)
    GPIO.output(a[2], 0)
    GPIO.output(a[3], 0)
    GPIO.output(a[4], 0)
    GPIO.output(a[5], 0)
    GPIO.output(a[6], 0)
    GPIO.output(a[7], 0)





    N = 7
    p = 0
    x = []

    while N>0:
        p = int(number/2**N)
        if p==1:
            x.append(1)
            number -=2**N
        else:
            x.append(0)
        N -= 1
    x.append(number)

    #x = decToBinList(number)
    i = 0
    #print (x)
    while i < 8:
        if x[i] >0:
           GPIO.output(a[7-i], 1)
        i = i+1

#lightNumber(5)

def runningPattern(pattern, direction):
    GPIO.output(a[0], 0)
    GPIO.output(a[1], 0)
    GPIO.output(a[2], 0)
    GPIO.output(a[3], 0)
    GPIO.output(a[4], 0)
    GPIO.output(a[5], 0)
    GPIO.output(a[6], 0)
    GPIO.output(a[7], 0)
    N = 7
    p = 0
    x = []

    while N>0:
        p = int(pattern/2**N)
        if p==1:
            x.append(1)
            pattern -=2**N
        else:
            x.append(0)
        N -= 1
    x.append(pattern)
    b=[0,0,0,0,0,0,0,0]
    i=0
    while i<8:
        if x[i] > 0:
            b[(i + direction) % 8] = 1
            i = i+1
    print (b)
    j=0
    while j < 8:
        if b[j] >0:
           GPIO.output(a[7-j], 1)
        j = j+1
        
runningPattern(5, 1)
