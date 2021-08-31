import grpc
from datetime_pb2 import DateTimeRequest
from datetime_pb2_grpc import PredictionStub

if __name__ == '__main__':
    # На порту 50051 мы создали соединение с localhost, то есть вашей собственной машиной
    stub = grpc.insecure_channel("localhost:50051")

    # Затем мы передаем канал PredictionStub, чтобы создать экземпляр клиента
    client = PredictionStub(stub)

    # Запрос
    request =DateTimeRequest(
        day=21,
        time=11
    )

    response = client.Predict(request)
    print(response)