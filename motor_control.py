import RPi.GPIO as IO

print("Start")
pwm_pin = 25
pin_1 = 23
pin_2 = 24
frequency = 1000
IO.setmode(IO.BCM)

print("A")
IO.setup(pin_1, IO.OUT)
print("B")
IO.setup(pin_2, IO.OUT)
print("C")
IO.setup(pwm_pin, IO.OUT)
print("Set frequncy{}".format(frequency))
pwm = IO.PWM(pwm_pin, frequency)
pwm.start(0)

def change(speed, direction):
    pwm.ChangeDutyCycle(speed)
    IO.output(pin_1,direction)
    IO.output(pin_2,not direction)

def fordward(speed):
    change(speed, True)

def backward(speed):
    change(speed, False)


if __name__ == '__main__':
    print("starting main")
    try:
        print("Inside try")
        while True:
            print("Loop")
            speed = int(raw_input("Enter Speed: "))
            direction_char = raw_input("Forward [Y/N]?").strip().lower()
            if direction_char[0] == 'y':
                print("Forward, speed {}".format(speed))
                fordward(speed)
            else:
                print("Backward, speed {}".format(speed))
                backward(speed)
    except:
        print("Killed")
        raise

    IO.cleanup()
