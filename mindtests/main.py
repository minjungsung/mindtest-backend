import os
import sys
import grpc
import asyncio
from concurrent import futures
from dotenv import load_dotenv

from mindtests import grpc_handler
from pyproto import mindtest_pb2, mindtest_pb2_grpc


class MindTestService(mindtest_pb2_grpc.ServerServicer):
    def web_to_server(self, request, context):
        return grpc_handler(request)

    def server_to_web(self, request, context):
        return mindtest_pb2.ServerToWebResponse(mbti_result=mindtest_pb2.MBTIResultResponse(type=mindtest_pb2.MBTIType.INTJ, description="Introverted, Intuitive, Thinking, Judging"))

def serve():
    # Load environment variables from .env file
    load_dotenv()
    # Replace placeholder with the current working directory
    project_root = os.getcwd()
    pythonpath = os.getenv('PYTHONPATH').replace('PROJECT_ROOT', project_root)

    # Set the PYTHONPATH environment variable dynamically
    os.environ['PYTHONPATH'] = pythonpath

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mindtest_pb2_grpc.add_ServerServicer_to_server(MindTestService(), server)

    server.add_insecure_port(f'[::]:{os.environ.get("GRPC_SERVER_PORT")}')
    server.start()

    print(f"Server started on port {os.environ.get('GRPC_SERVER_PORT')}")
    server.wait_for_termination(None)

if __name__ == '__main__':
    try:    
        serve()
    except KeyboardInterrupt:
        print("Server interrupted by user")
    except Exception as e:
        print(f"Server error: {e}")