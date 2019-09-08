
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
    thetak = []
    Q = n.matrix([[.001, 0], [0, .003]])
    R = .03
    I = n.matrix([[1, 0], [0, 1]])
    H = n.matrix([1, 0])
    P = []
    N = 3
    for i in range(0,N):
        P.append(n.matrix([[1000, 0], [0, 1000]]))
        thetak.append(n.matrix([[0], [0]]))
    while True:
        try:
            data = device.readData() #n.multiply(data,beta) + n.multiply(device.readData(), alpha)
            later = datetime.now()
            diff = later-now
            dt = diff.microseconds/MICRO_TO_SECOND
            now = later
            acc_zx_angle = M.degrees(M.atan2(data[5],data[3]))
            acc_yz_angle = M.degrees(M.atan2(data[4],data[5]))
            acc_xy_angle = M.degrees(M.atan2(data[3],data[4]))
            acc_angle = [acc_yz_angle, acc_zx_angle, acc_xy_angle]
            F = n.matrix([[1, -dt], [0, 1]])
            B = n.matrix([[dt], [0]])

            output = "dt %.5f" % (dt)
            for i in range(0, 3):
                m = n.matrix(data[i])
                thetak_1 = F*thetak[i] + B*m
                P[i] = F*P[i]*F.transpose() + Q
                yk = acc_angle[i] - H*thetak_1
                S = H*P[i]*H.transpose() + R
                K = P[i]*H.transpose()*S.getI()
                thetak[i] = thetak[i] + K*yk
                P[i] = (I - H*K)*P[i]
                output += " %i angle %.5f offset %.5f " % (i, thetak[i].item(0), thetak[i].item(1))

            print(output, end='\r')
        except KeyboardInterrupt:
            break

    print("\nEnding")