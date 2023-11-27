# calculator_client.py
import json

import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    for i in range(1, 100):
        if i != 1:
            request = calculator_pb2.Request(kwargs=json.dumps({"type": "update_data", "db_data": {"name": "damon"}}))
        else:
            request = calculator_pb2.Request(kwargs=json.dumps({"type": "optim"}))
        response = stub.ProcessRequests(request)
        print(response.result)


if __name__ == '__main__':
    run()
