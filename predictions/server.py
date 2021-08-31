from concurrent import futures
import grpc
from datetime_pb2 import TimePrediction
import datetime_pb2_grpc
import pickle


class PredictionService(datetime_pb2_grpc.PredictionServicer):
    def Predict(self, request, context):
        print("send response")
        return TimePrediction(time=model(request))


def model(x):
    query = [[x.day] + [0 for i in range(24)]]
    query[0][x.time + 1] = 1
    return lin_reg.predict(query)[0]


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datetime_pb2_grpc.add_PredictionServicer_to_server(
        PredictionService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    with open("lin_reg.pkl", 'rb') as file:
        lin_reg = pickle.load(file)
    serve()