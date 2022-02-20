FROM golang:1.17

EXPOSE 50051

WORKDIR /app
COPY . .

RUN apt update && apt install protobuf-compiler -fy

RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.27
RUN go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.2
RUN export PATH="$PATH:$(go env GOPATH)/bin"

RUN go build grpc_client.go
RUN go build grpc_server.go

CMD ["./grpc_server"]
