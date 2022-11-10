import logging
from concurrent import futures

import grpc
import access_code_pb2
import access_code_pb2_grpc

import datetime


class AccessCodeServiceServicer(access_code_pb2_grpc.AccessCodeServiceServicer):
    def AppendPhoneNumber(self, request, context):
        print(request.phone_number)
        reply = access_code_pb2.AppendPhoneNumberResponse()
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    access_code_pb2_grpc.add_AccessCodeServiceServicer_to_server(AccessCodeServiceServicer(), server)
    server.add_insecure_port("localhost:500511")
    server.start()
    print(str(datetime.datetime.now()) + "server started on 500511")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
