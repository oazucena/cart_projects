import RPi.GPIO as G
import time as T
G.setmode(G.BCM)
G.setup(4, G.IN)

def main():
    print("main begin")

    last = G.input(4)
    print("last = %d"%(last))
    while True:
        current = G.input(4)
        if current != last:
            last = current
            print("last = %d"%(last))


if __name__ == "__main__":
    main()
