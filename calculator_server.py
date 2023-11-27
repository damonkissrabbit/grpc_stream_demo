import json
import grpc
import calculator_pb2
import calculator_pb2_grpc
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor, wait


class Optim(object):
    def __init__(self):
        self.db_data = {}

    def cost_function(self, i):
        calculator_pb2.Response(result=i)
        flag = True
        while flag:
            if self.db_data:
                db_data = self.db_data
                self.db_data = {}
                flag = False
        return i / 2

    def optimize(self):
        sum_value = 0
        for i in range(1, 10):
            sum_value += self.cost_function(i)
        calculator_pb2.Response(result=sum_value * 10)

    def thread_option(self, db_data):
        self.db_data = db_data


op = Optim()


def choice_func(kwargs):
    if kwargs["type"] == "optim":
        op.optimize()
    else:
        op.thread_option(kwargs["db_data"])


excutor = ThreadPoolExecutor(max_workers=2)


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def ProcessRequests(self, request, context):
        infos = json.loads(request.kwargs)
        all_task = [excutor.submit(choice_func, infos)]
        wait(all_task)
        # calculator_pb2.Response(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
