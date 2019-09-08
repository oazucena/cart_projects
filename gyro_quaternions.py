
import gyro as G
import math as M
import numpy as n
import quaternion as Q
from datetime import datetime
from time import sleep

MICRO_TO_SECOND = 1000000.0

def toEuler(q) :
    # roll (x-axis rotation)
    sinr_cosp = 2.0 * (q.w * q.x + q.y * q.z)
    cosr_cosp = +1.0 - 2.0 * (q.x * q.x + q.y * q.y)
    roll = M.atan2(sinr_cosp, cosr_cosp)

    # pitch (y-axis rotation)
    sinp = +2.0 * (q.w * q.y - q.z * q.x)
    pitch = M.asin(sinp)
    if M.fabs(sinp) >= 1:
        pitch =M.copysign(M_PI / 2, sinp)
        

    # yaw (z-axis rotation)
    siny_cosp = +2.0 * (q.w * q.z + q.x * q.y);
    cosy_cosp = +1.0 - 2.0 * (q.y * q.y + q.z * q.z);  
    yaw = M.atan2(siny_cosp, cosy_cosp);

    return [roll, pitch, yaw]

if __name__ == "__main__":
    device = G.GY521()
    values = device.readData()
    device.setAccelerationRange(16)
    quat = n.quaternion(1.0,0.0,0.0,0.0)
    vector = n.quaternion(0.0,0.0,0.0,1.0)
    alpha= 0.1
    beta = 1.0-alpha
    dt = 0
    angle_zx = 0
    angle_yz = 0
    angle_xy = 0
    now = datetime.now()
    data = [0 for x in range(0,6)]
    output = "dt: % .5f x:  % .5f " % (dt, quat.w)
    print(output)
    while True:
        try:
            data = device.readData()

            sw = Q.quaternion(0.0, data[0], data[1], data[2])
            qdot=0.5*(quat*sw)
            later = datetime.now()
            diff = later-now
            dt = diff.microseconds/MICRO_TO_SECOND
            now =  datetime.now()
            quat=quat + qdot*dt
            quat = quat.normalized()

            r = quat*vector*quat.conjugate()
            output = "dt: % .5f x:  % .5f y:  % .5f z:  % .5f " % (dt, r.x, r.y, r.z)
            print(output, end='\r')
        except KeyboardInterrupt:
            break

    print("\nEnding")