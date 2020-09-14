python3 -m grpc_tools.protoc -I./grpc_car_files/ --python_out=grpc_car_files/ --grpc_python_out=grpc_car_files/ grpc_car_files/car.proto

# Change import as currently GPRC does not generated correct python3
# for importing the file from the same directory
sed -i 's/import car_pb2/from . import car_pb2/g' ./grpc_car_files/car_pb2_grpc.py
