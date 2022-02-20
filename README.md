# gRPC Benchmarks

## Building and running

### Go

```bash
# Build docker image
cd go
docker build -t grpc-go .

# Run server/client
docker run -it grpc-go
docker run -it grpc-go ./grpc_client

# Alternatively...

# Run in development mode
docker run -it --rm --name=grpc-go -p 50051:50051 -v ${PWD}:/app grpc-go bash

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
docker run -it grpc-python
docker run -it grpc-python python grpc_client.py

# Alternatively...

# Run in development mode
docker run -it --rm --name=grpc-python -p 50051:50051 -v ${PWD}:/app grpc-python bash

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
