```bash
# Build docker image
docker build -t grpc-python .

# Run in development mode
docker run -it --rm --name=grpc-python -p 50051:50051 -v ${PWD}:/app grpc-python bash

# Within docker container...

# Generate gRPC code
./generate_grpc_code.sh

# Run server and client
python grpc_server.py &
python grpc_client.py
```
