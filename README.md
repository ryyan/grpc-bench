# gRPC Benchmarks

## Building and running

### Go

```bash
# Build docker image
cd go
docker build -t grpc-go .

# Run server/client
docker run -it -d --net="host" --name grpc-server grpc-go
docker run -it --net="host" --name grpc-client grpc-go ./grpc_client

# Stop server
docker kill grpc-server
docker rm grpc-server
```

```bash
# Alternatively...

# Run in development mode
docker run -it --rm --name=grpc-go --net="host" -v ${PWD}:/app grpc-go bash

# Within docker container...

# Generate gRPC code (optional)
cd proto
./generate_grpc_code.sh
cd ..

# Build server/client
go build grpc_server.go
go build grpc_clent.go

# Run server/client
./grpc_server &
./grpc_client
```

### Python

```bash
# Build docker image
cd python
docker build -t grpc-python .

# Run server/client
docker run -it -d --net="host" --name grpc-server grpc-python
docker run -it --net="host" --name grpc-client grpc-python python grpc_client.py
docker kill grpc-server

# Stop server
docker kill grpc-server
docker rm grpc-server
```

```bash
# Alternatively...

# Run in development mode
docker run -it --rm --name=grpc-python --net="host" -v ${PWD}:/app grpc-python bash

# Within docker container...

# Generate gRPC code (optional)
cd proto
./generate_grpc_code.sh
# Update hello_pb2_grpc.py import to use local directory, for example:
# from . import hello_pb2 as hello__pb2
# Otherwise you'll get ModuleNotFoundError: No module named 'hello_pb2'
cd ..

# Run server and client
python grpc_server.py &
python grpc_client.py
```

## Benchmark Results

Benchmarking was done by

1. Starting each server using their `docker run -it -d ...` command (one at a time)
2. Running each client in development mode
3. Within the client container, running the client with `time`

| Server | Client | Time (Real) |
| ------ | ------ | ----------- |
| Go     | Go     | 0m0.005s    |
| Go     | Python | 0m0.077s    |
| Python | Python | 0m0.078s    |
| Python | Go     | 0m0.006s    |

```bash
$ docker --version
Docker version 20.10.7, build 20.10.7-0ubuntu5~21.04.2

# Below commands were ran inside each respective dev container

$ go version
go version go1.17.7 linux/amd64

$ python --version
Python 3.9.5

$ pip list
Package      Version
------------ -------
grpcio       1.44.0
grpcio-tools 1.44.0
pip          22.0.3
protobuf     3.19.4
setuptools   58.1.0
six          1.16.0
wheel        0.37.1
```
