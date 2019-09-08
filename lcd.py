import socket
import time
from RPLCD.i2c import CharLCD
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():

    lcd = CharLCD(i2c_expander='PCF8574', address=0x3F, port=1,
              cols=15, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)
    while True:
        ip = get_ip()
        lcd.clear()
        print("IP Address: %s" % (ip))
        lcd.write_string(ip)
        if ip != '127.0.0.1':
            break
        time.sleep(3)

if __name__ == '__main__':
    main()
    
     
