#!/usr/bin/env python3

from concurrent import futures
import io
import base64
import argparse
import grpc
from PIL import Image
import lab6_pb2
import lab6_pb2_grpc


def imageSize(data):
    try:
        img = Image.open(io.BytesIO(data))
        return lab6_pb2.imageReply(width=img.size[0], height=img.size[1])
    except:
        return lab6_pb2.imageReply(width=0, height=0)


class Lab6Servicer(lab6_pb2_grpc.Lab6Servicer):
    def add(self, request, context):
        return lab6_pb2.addReply(sum=request.a + request.b)

    def rawImage(self, request, context):
        return imageSize(request.img)

    def dotProduct(self, request, context):
        return lab6_pb2.dotProductReply(dotproduct=sum(x * y for x, y in zip(request.a, request.b)))

    def jsonImage(self, request, context):
        return imageSize(base64.b64decode(request.img))


parser = argparse.ArgumentParser(description='gRPC server')
parser.add_argument('-p', '--port', type=int, default=50051, help='Server port (default: 50051)')
args = parser.parse_args()

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
lab6_pb2_grpc.add_Lab6Servicer_to_server(Lab6Servicer(), server)
server.add_insecure_port(f'[::]:{args.port}')
server.start()
server.wait_for_termination()
