import sys
import os
import asyncio
from concurrent import futures

import grpc
from mindtests.pyproto import mindtest_pb2_grpc
from mindtests.pyproto import mindtest_pb2

# Ensure pyproto is in the Python path
print(os.path.join(os.path.dirname(__file__), "pyproto"))

# import pyproto.mindtest_pb2 as mindtest_pb2
# import pyproto.mindtest_pb2_grpc as mindtest_pb2_grpc


class MindTestService(mindtest_pb2_grpc.ServerServicer):
    def web_to_server(self, request, context):
        return mindtest_pb2.WebToServiceResponse(
            test=mindtest_pb2.MindTest(id=1, type=mindtest_pb2.MindTestType.MBTI)
        )

    def server_to_web(self, request, context):
        return mindtest_pb2.ServiceToWebResponse(
            mbti_result=mindtest_pb2.MBTIResultResponse(
                type=mindtest_pb2.MBTIType.INTJ,
                description="Introverted, Intuitive, Thinking, Judging",
            )
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mindtest_pb2_grpc.add_ServerServicer_to_server(MindTestService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
