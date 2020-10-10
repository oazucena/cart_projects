import numpy as np
from numpy import matmul as mm
from numpy import transpose as transpose
from numpy import linalg as la
from datetime import datetime as datetime
import gyro as GY
import time

def getKFA(dt):
    hd = dt*dt/2.0
    A = np.array([[1, 0, 0, dt, 0, 0, hd, 0, 0],
                 [0, 1, 0, 0, dt, 0, 0, hd, 0],
                 [0, 0, 1, 0, 0, dt, 0, 0, hd],
                 [0, 0, 0, 1, 0, 0, dt, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, dt, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, dt],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1]])
    return A

def getKFH():
    H = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1]])
    return H

def getError(e):
    E = np.array([[e, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, e, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, e, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, e, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, e, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, e, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, e, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, e, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, e]])
    return E  

def getErrorFull(e):
    E = np.array([[e, e, e, e, e, e, e, e, e],
                 [e, e, e, e, e, e, e, e, e],
                 [e, e, e, e, e, e, e, e, e],
                 [e, e, e, e, e, e, e, e, e],
                 [e, e, e, e, e, e, e, e, e],
                 [e, e, e, e, e, e, e, e, e],
                 [e, e, e, e, e, e, e, e, e],
                 [e, e, e, e, e, e, e, e, e],
                 [e, e, e, e, e, e, e, e, e]])
    return E  

def getCovariance(A,B,E):
    res = mm(A,B)
    res = mm(res,transpose(A))
    res = res + E
    return res

def getPredCoVar(A, P, Q):
    return getCovariance(A, P, Q)

def getInoCoVar(H, P, R):
    return getCovariance(H, P, R)

def getNewX(A, x):
    return mm(A, x)

def getDeltaTime(t1, t0):
    dt = t1 - t0
    return dt.total_seconds()

def getKGain(P, H, S):
    res = mm(P,transpose(H))
    res = mm(res,la.pinv(S))
    return res

def getInnovation(z, H, x):
    return z - mm(H, x)

def getUpdate(K, y):
    return mm(K, y)

def getUpdatedCovariance(I, K, H, P):
    res = mm(K,H)
    res = I - res
    res = mm(res, P)
    return res

def getNewMeasurement(device):
    data = device.readData()
    # substrack gravity
    return np.array([[0], [0], [0], [0], [0], [0], [data[3]], [data[4]], [data[5] - 1.0]])

def printVector(v):
    print("{} {} {} {} {} {} {} {} {} ".format(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8]))

class KalmanFilter:
    def __init__(self, device):
        self.dev = device
        self.t0 = None
        self.x = np.array([[0], [0], [0], [0], [0], [0], [0], [0], [0]])
        self.P = getError(1000)
        self.Q = 0.1
        self.R = 0.1
        self.H = getKFH()
        self.I = getError(1.0)

    def getData(self):
        if self.t0 == None:
            self.t0 = datetime.now()
            return self.x
            
        now = datetime.now()
        dt = getDeltaTime(now,self.t0)
        self.t0 = now

        A = getKFA(dt)
        self.x = getNewX(A, self.x)
        self.P = getPredCoVar(A, self.P, self.Q)
        z = getNewMeasurement(self.dev)
        printVector(z)
        y = getInnovation(z, self.H, self.x)
        self.S = getInoCoVar(self.H, self.P, self.R)
        K = getKGain(self.P, self.H, self.S)
        self.x = self.x + getUpdate(K, y)        
        self.P = getUpdatedCovariance(self.I, K, self.H, self.P) 

        return self.x


def serve():
    device = GY.GY521()
    KF = KalmanFilter(device)
    
    while True:
        x = KF.getData()
        printVector(x)
        time.sleep(0.033) 



if __name__ == '__main__':
    serve()
    print("Closing KF")
