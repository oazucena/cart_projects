import gyro as G
import math as M
import numpy as n
from datetime import datetime
from time import sleep

MICRO_TO_SECOND = 1000000.0

class ComplementaryFilter:
    def __init__(self, gyro, alpha):
        self.device = gyro
        self.alpha = alpha
        self.beta = 1.0-alpha
        self.device.setAccelerationRange(16)
        self.angle_zx = 0
        self.angle_yz = 0
        self.angle_xy = 0
        self.last = datetime.now()

    def readData(self):
        data = self.device.readData() #n.multiply(data,beta) + n.multiply(device.readData(), alpha)
        later = datetime.now()
        diff = later-self.last
        self.last = later
        dt = diff.microseconds/MICRO_TO_SECOND
        acc_zx_angle = M.degrees(M.atan2(data[5],data[3]))
        acc_yz_angle = M.degrees(M.atan2(data[4],data[5]))
        acc_xy_angle = M.degrees(M.atan2(data[3],data[4]))

        self.angle_zx = self.beta*(self.angle_zx + dt*data[1]) + self.alpha*acc_zx_angle
        self.angle_yz = self.beta*(self.angle_yz + dt*data[0]) + self.alpha*acc_yz_angle
        self.angle_xy = self.beta*(self.angle_xy + dt*data[2]) + self.alpha*acc_xy_angle
        self.acc_x = data[3]
        self.acc_y = data[4]
        self.acc_z = data[5]
        return [self.angle_zx, self.angle_yz, self.angle_xy, self.acc_x, self.acc_y, self.acc_z, dt]

if __name__ == "__main__":
    device = G.GY521()
    CF = ComplementaryFilter(device, 0.1)
    while True:
        try:
            data = CF.readData()
            output = "dt:% .5f zx:% .5f , yz:% .5f , xy:% .5f , ax:% .5f, ay:% .5f, az:% .5f" % (data[6], data[0], data[1], data[2], data[3], data[4], data[5])
            print(output, end='\r')
        except KeyboardInterrupt:
            break

    print("\nEnding")
