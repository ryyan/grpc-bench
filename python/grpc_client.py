import asyncio
import logging

import grpc

import proto.hello_pb2 as hello_pb2
import proto.hello_pb2_grpc as hello_pb2_grpc

async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(hello_pb2.HelloRequest(name="world"))

    print(response.message)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
