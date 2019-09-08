import RPi.GPIO as IO

frequency = 100
class Wheel:
    def __init__(self, pwm, p1, p2):
        self.pwm_pin = pwm
        self.p1 = p1
        self.p2 = p2
        IO.setup(self.p1, IO.OUT)
        IO.setup(self.p2, IO.OUT)
        IO.setup(self.pwm_pin, IO.OUT)
        self.pwm = IO.PWM(self.pwm_pin, frequency)
        self.pwm.start(0)

    def fordward(self, speed):
        self.change(speed, True)
    def backward(self, speed):
        self.change(speed, False)
    def change(self, speed, direction):
        self.pwm.ChangeDutyCycle(speed)
        IO.output(self.p1, direction)
        IO.output(self.p2, not direction)


if __name__ == '__main__':
    wtr = Wheel(27, 5, 22)
    wtl = Wheel(19, 13, 6)
    wbr = Wheel(18, 24, 23)
    wbl = Wheel(16, 12, 25)
    print("starting main")
    try:
        print("Inside try")
        while True:
            print("Loop")
            speed = int(raw_input("Enter Speed: "))
            direction_char = raw_input("Forward [Y/N]?").strip().lower()
            if direction_char[0] == 'y':
                print("Forward, speed {}".format(speed))
                wtr.fordward(speed)
                wtl.fordward(speed)
                wbr.fordward(speed)
                wbl.fordward(speed)
            else:
                print("Backward, speed {}".format(speed))
                wtr.backward(speed)
                wtl.backward(speed)
                wbr.backward(speed) 
                wbl.backward(speed)
                
    except:
        print("Killed")
        raise

    IO.cleanup()
