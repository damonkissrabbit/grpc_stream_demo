# calculator_client.py
import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # 向服务端发送多个请求
    for i in range(100):
        request = calculator_pb2.Request(num1=i, num2=i + 1)
        response = stub.ProcessRequests(iter([request]))
        result = next(response)
        print(f"Result for request {i}: {result.result}")


if __name__ == '__main__':
    run()
