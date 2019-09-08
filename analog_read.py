import smbus as BUS
import time as T
import step_motor_self as motor

address = 0x48
bus = BUS.SMBus(1)
cmd = 0x40

def analogRead(ch) :
    value = bus.read_byte_data(address,cmd+ch)
    return value

def analogWrite(val):
    bus.write_byte_data(address, cmd, val)

def loop():
    lastRotation = 0
    lastValue = 0
    while True:
        value = analogRead(0)
        analogWrite(value)
        voltage = value/255.0*5.0
        rotation = int(value/255.0*500)
        if rotation == lastRotation:
             lastRotation=rotation
        elif rotation > lastRotation:
            motor.fordward(.001, rotation-lastRotation)
        else:
            motor.backward(.001, lastRotation-rotation)
        lastRotation = rotation
        if lastValue != value:
            lastValue = value
            print("ADC value: %d, VOltage: %.2f"%(value, voltage))
        T.sleep(0.01)

def destroy():
    bus.close()

if __name__ == "__main__":
    print("Program starting...")
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

