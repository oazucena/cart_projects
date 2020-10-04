import bluetooth
import Car as Car
import gyro as GY
import RPi.GPIO as G
from concurrent import futures
import logging
import threading

import grpc

from random import gauss

import grpc_car_files.car_pb2 as car_pb2
import grpc_car_files.car_pb2_grpc as car_pb2_grpc

import queue
import time

import complementary_filter as CFF

G.setmode(G.BOARD)

class OmniCar(Car.Car):
    def right(self, speed):
        self.wtl.fordward(speed)
        self.wtr.backward(speed)
        self.wbr.backward(speed)
        self.wbl.fordward(speed)
    
    def left(self, speed):
        self.wtl.backward(speed)
        self.wtr.fordward(speed)
        self.wbr.fordward(speed)
        self.wbl.backward(speed)

wheels = {"top_right":{"name":"top_right","e":32,"f":24,"r":26},\
            "top_left":{"name":"top_left", "e":19,"f":23,"r":21},\
            "bottom_right":{"name":"bottom_right", "e":22,"f":18,"r":16},\
            "bottom_left":{"name":"bottom_left", "e":11,"f":15,"r":13}}
car = OmniCar(wheels)
q = queue.Queue(10)
stop_stream = False
return_data = True
class CarServer(car_pb2_grpc.CarServicer):
    def __init__(self):
        self.stop_stream = True

    def direction(self, request, context):
        print("request {}".format(request))
        if request.direction == car_pb2.Direction.FORWARD:
            car.fordward(request.speed)
        elif request.direction == car_pb2.Direction.BACKWARD:
            print("Backward")
            car.backward(request.speed) 
        elif request.direction == car_pb2.Direction.RIGHT:
            print("Right")
            car.right(request.speed) 
        elif request.direction == car_pb2.Direction.LEFT:
            print("Left")
            car.left(request.speed)   
        elif request.direction == car_pb2.Direction.STOP:
            print("Stop")
            car.stop()
        return car_pb2.DirectionReply(message='Direction {}, Speed {}!'.format(car_pb2.Direction.Name(request.direction), request.speed))

    def stop(self, request, context):
        print("stop stream")
        self.stop_stream = True
        return car_pb2.Empty()

    def state(self, request_iterator, context):
        self.stop_stream = False
        print("Start Stream")
        while not self.stop_stream and context.is_active():
            item = q.get(block=True, timeout=1)
            q.task_done()
            yield item
        print("Stop State")


def readAccelerations(device):
    while True:
        data = device.readData()
        acceleration = car_pb2.Acceleration(x=data[3], y=data[4], z=data[5])
        state_info = car_pb2.CarStateInfo(acceleration=acceleration)
        q.put(state_info)
        time.sleep(.05)

def serve():
    device = GY.GY521()
    CF = CFF.ComplementaryFilter(device, 0.1)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    car_pb2_grpc.add_CarServicer_to_server(CarServer(), server)
    server.add_insecure_port('[::]:50051')
    threading.Thread(target=readAccelerations, args=(CF,), daemon=True).start()
    print("Start server")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
    G.cleanup()
    print("Closing Car Server")
