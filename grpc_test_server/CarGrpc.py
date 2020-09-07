import bluetooth
import ../Car as Car
import RPi.GPIO as G
from concurrent import futures
import logging

import grpc

import grpc_test_server.car_pb2 as car_pb2
import grpc_test_server.car_pb2_grpc as car_pb2_grpc

import queue
import time

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
queue = queue.Queue()
stop_stream = True
class CarServer(car_pb2_grpc.CarServicer):
    
    def direction(self, request, context):
        print("request {}".format(request))
        if request.direction == car_pb2.Direction.FORWARD:
            car.fordward(request.speed)
        if request.direction == car_pb2.Direction.BACKWARD:
            print("Backward")
            car.backward(request.speed) 
        if request.direction == car_pb2.Direction.RIGHT:
            print("Right")
            car.right(request.speed) 
        if request.direction == car_pb2.Direction.LEFT:
            print("Left")
            car.left(request.speed)   
        if request.direction == car_pb2.Direction.STOP:
            print("Stop")
            car.stop()
        return car_pb2.DirectionReply(message='Direction {}, Speed {}!'.format(car_pb2.Direction.Name(request.direction), request.speed))

    def state(self, request_iterator, context):
        stop_stream = False
        while not stop_stream:
            item = q.get(block=True, timeout=1)
            q.task_done()
            yield item
            
def generateAccelerations():
    while True:
        acceleration = car_pb2.Acceleration(x=10, y=10, z=10)
        state_info = car_pb2.CarStateInfo(acceleration=acceleration)
        q.put(state_info)
        time.sleep(.005)
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    car_pb2_grpc.add_CarServicer_to_server(CarServer(), server)
    server.add_insecure_port('[::]:50051')
    print("Start server")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
    G.cleanup()
    print("Closing Car Server")
