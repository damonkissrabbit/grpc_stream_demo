# calculator_server.py
import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def ProcessRequests(self, request_iterator, context):
        sum = 0
        for request in request_iterator:
            print(request)
            result = request.num1 + request.num2
            sum += result
            print(sum)

            # 返回结果给客户端
            yield calculator_pb2.Response(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
