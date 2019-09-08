#!/usr/bin/python3
import smbus
import math 
import sys
import numpy

ACC_SCALE_2G = 16384.0
ACC_SCALE_4G = 8192.0
ACC_SCALE_8G = 4096.0
ACC_SCALE_16G = 2048.0

GYR_SCALE_250 = 131.0
GYR_SCALE_500 = 65.5
GYR_SCALE_1000 = 32.8
GYR_SCALE_2000 = 16.4

DEF_ADDRESS = 0x68

ACC_CONFIG_REG = 0x1C
ACC_X_REG = 0x3B
ACC_Y_REG = 0x3D
ACC_Z_REG = 0x3F

GYR_X_REG = 0x43
GYR_Y_REG = 0x45
GYR_Z_REG = 0x47

XA_OFFSET_REG = 6
YA_OFFSET_REG = 8
ZA_OFFSET_REG = 10

XG_OFFSET_REG = 0x13
YG_OFFSET_REG = 0x15
ZG_OFFSET_REG = 0x17


# Register
POWER_MGMT = 0x6b
power_mgmt_2 = 0x6c
  
def read_byte(bus, address, reg):
    return bus.read_byte_data(address, reg)
       
def read_word(bus, address, reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
                       
def write_word(bus, address, reg, data):
    print("raw %d to %d" % (data, reg))
    data = convert_to_2c(data)
    bus.write_byte_data(address, reg, (data & 0x00FF00) >> 8)
    bus.write_byte_data(address, reg+1, data & 0x00FF)
    print("writing %04X to %d" % (data, reg))
    print("wrote %04X to %d" % (read_byte(bus, address, reg), reg))
    print("wrote %04X to %d\n" % (read_byte(bus, address, reg+1), reg+1))

def convert_to_2c(val):
    return (val ^ 65535) + 1

def convert_from_2c(val):
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
    
def read_word_2c(bus, address, reg):
    val = read_word(bus, address, reg)
    return convert_from_2c(val)
            
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
                                                           
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
                                                                   
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def write_accel_calibration(bus,address,x,y,z):
    write_word(bus, address, XA_OFFSET_REG, int(x * ACC_SCALE_16G))
    write_word(bus, address, YA_OFFSET_REG, int(y * ACC_SCALE_16G))
    write_word(bus, address, ZA_OFFSET_REG, int(z * ACC_SCALE_16G))

def write_gyro_calibration(bus,address,x,y,z):
    write_word(bus, address, XG_OFFSET_REG, int(x * GYR_SCALE_2000))
    write_word(bus, address, YG_OFFSET_REG, int(y * GYR_SCALE_2000))
    write_word(bus, address, ZG_OFFSET_REG, int(z * GYR_SCALE_2000))

def read_acceleration(bus, address, reg, scale):
    return read_word_2c(bus, address, reg) / scale

def read_gyro(bus, address, reg, scale):
    return read_word_2c(bus,address, reg) / scale

class GY521 :
    def __init__(self):
        self.bus = smbus.SMBus(1) # bus = smbus.SMBus(0) for Revision 1
        self.address = 0x68
        self.getAccelerationScale()
        self.gyr_scale = GYR_SCALE_250
    def readData(self):
        self.bus.write_byte_data(self.address, POWER_MGMT, 0)

        self.g_x = read_gyro(self.bus, self.address, GYR_X_REG, GYR_SCALE_250)
        self.g_y = read_gyro(self.bus, self.address, GYR_Y_REG, GYR_SCALE_250)
        self.g_z = read_gyro(self.bus, self.address, GYR_Z_REG, GYR_SCALE_250)
                                                                              
        self.a_x = read_acceleration(self.bus, self.address, ACC_X_REG, self.acc_scale)
        self.a_y = read_acceleration(self.bus, self.address, ACC_Y_REG, self.acc_scale)
        self.a_z = read_acceleration(self.bus, self.address, ACC_Z_REG, self.acc_scale)
        self.rotation_x = get_x_rotation(self.a_x, self.a_y, self.a_z)
        self.rotation_y = get_y_rotation(self.a_x, self.a_y, self.a_z)
        return [self.g_x, self.g_y, self.g_z, self.a_x,self.a_y, self.a_z]

    def calibrate(self, loop):
        self.ma_x = 0
        self.ma_y = 0
        self.ma_z = 0

        self.mg_x = 0
        self.mg_y = 0
        self.mz_z = 0

        
        self.va_x = 0
        self.va_y = 0
        self.va_z = 0

        self.vg_x = 0
        self.vg_y = 0
        self.vg_z = 0

        self.ma = [0 for x in range(0,6)]
        self.va = [0 for x in range(0,6)]
        write_accel_calibration(self.bus, self.address, self.ma_x, self.ma_y, self.ma_z)
        write_gyro_calibration(self.bus, self.address, self.ma_x, self.ma_y, self.ma_z)

        count = 0
        if True:
            while True:
                data = self.readData()
                self.ma = numpy.add(self.ma, data)
                self.va = numpy.add(self.va, numpy.square(data))

                count += 1
                if loop <= count:
                    break      
            self.ma = numpy.true_divide(self.ma, count)
            print(self.ma)

            write_accel_calibration(self.bus, self.address, self.ma[3], self.ma[4], (self.ma[5]-1))
            write_gyro_calibration(self.bus, self.address, self.ma[0],self.ma[1], self.ma[2])
            self.va = self.va - count*numpy.square(self.ma)
            self.va = numpy.sqrt(numpy.true_divide(self.va,count-1))

            print("offset g_x: {} variance: {}".format(self.ma[0], self.va[0]))
            print("offset g_y: {} variance: {}".format(self.ma[1], self.va[1]))
            print("offset g_z: {} variance: {}".format(self.ma[2], self.va[2]))

            print("offset a_x: {} variance: {}".format(self.ma[3], self.va[3]))
            print("offset a_y: {} variance: {}".format(self.ma[4], self.va[4]))
            print("offset a_z: {} variance: {}".format(self.ma[5], self.va[5]))

    def setAccelerationRange(self, range):
        config = read_byte(self.bus, self.address, ACC_CONFIG_REG)
        if range == 2 :
            config = config | 0b00000000
        if range == 4 :
            config = config | 0b00001000
        if range == 8 :
            config = config | 0b00010000
        if range == 16 :
            config = config | 0b00011000

        self.bus.write_byte_data(self.address, ACC_CONFIG_REG, config)
        self.getAccelerationScale()

    def getAccelerationScale(self):
        config = read_byte(self.bus, self.address, ACC_CONFIG_REG)
        print("config " + bin(config))
        config = config & 0b00011000
        config = config >> 3
        print("config " + bin(config))
        if config == 0:
            self.acc_scale = ACC_SCALE_2G
        if config == 1:
            self.acc_scale = ACC_SCALE_4G
        if config == 2:
            self.acc_scale = ACC_SCALE_8G
        if config == 3:
            self.acc_scale = ACC_SCALE_16G
        print("acceleration scale  %f" % (self.acc_scale))
    

if __name__ == "__main__":
    calibrate = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "calibrate":
            calibrate = True
    values = {}
    device = GY521()
    values = device.readData()
    device.setAccelerationRange(16)
    if calibrate:
        device.calibrate(10000)
    alpha= 0.2
    while True:
        try:
            data = device.readData()
            output = ""
            values = numpy.add(numpy.multiply(values,1.0-alpha), numpy.multiply(data, alpha))
            for val in data:
                output += " % .5f " % (val)
            print(output, end='\r')
        except KeyboardInterrupt:
            break

    print("\nEnding")

