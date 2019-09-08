
import gyro as G
import math as M
import numpy as n
from datetime import datetime
from time import sleep

MICRO_TO_SECOND = 1000000.0

if __name__ == "__main__":
    device = G.GY521()
    values = device.readData()
    device.setAccelerationRange(16)
    alpha= 0.1
    beta = 1.0-alpha
    dt = 0
    angle_zx = 0
    angle_yz = 0
    angle_xy = 0
    now = datetime.now()
    data = [0 for x in range(0,6)]
    while True:
        try:
            data = device.readData() #n.multiply(data,beta) + n.multiply(device.readData(), alpha)
            later = datetime.now()
            diff = later-now
            dt = diff.microseconds/MICRO_TO_SECOND
            now =  datetime.now()
            acc_zx_angle = M.degrees(M.atan2(data[5],data[3]))
            acc_yz_angle = M.degrees(M.atan2(data[4],data[5]))
            acc_xy_angle = M.degrees(M.atan2(data[3],data[4]))

            angle_zx = beta*(angle_zx + dt*data[1]) + alpha*acc_zx_angle
            angle_yz = beta*(angle_yz + dt*data[0]) + alpha*acc_yz_angle
            angle_xy = beta*(angle_xy + dt*data[2]) + alpha*acc_xy_angle

            output = "dt: % .5f zx:  % .5f , yz:  % .5f , xy:  % .5f " % (dt, angle_zx, angle_yz, angle_xy)
            print(output, end='\r')
        except KeyboardInterrupt:
            break

    print("\nEnding")