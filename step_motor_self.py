import RPi.GPIO as G
import time


G.setmode(G.BCM)

pin0=20
pin1=16
pin2=26
pin3=12

stepCount = 8
timeDelayUs = 1000 # us
seq = range(0,stepCount)
seq[0] = [0, 0, 0, 1]
seq[1] = [0, 0, 1, 1]
seq[2] = [0, 0, 1, 0]
seq[3] = [0, 1, 1, 0]
seq[4] = [0, 1, 0, 0]
seq[5] = [1, 1, 0, 0]
seq[6] = [1, 0, 0, 0]
seq[7] = [1, 0, 0, 1]


pins = [pin0,pin1,pin2,pin3]

for pin in pins:
    print "pin: ", pin
    G.setup(pin,G.OUT)
    G.output(pin,0)

def setStep(ws):
    for i in range(len(pins)):
        G.output(pins[i],ws[i])

def fordward(delay, steps):
    for i in range(steps):
        for j in range(stepCount):
            setStep(seq[j])
            time.sleep(delay)


def backward(delay, steps):
    for i in range(steps):
        for j in reversed(range(stepCount)):
            setStep(seq[j])
            time.sleep(delay)

if __name__ == '__main__':
    while True:
        steps = raw_input("Steps Forward?")
        fordward(float(int(timeDelayUs))/1000000.0, int(steps))
        steps = raw_input("Steps Backward?")
        backward(float(int(timeDelayUs))/1000000.0, int(steps))
