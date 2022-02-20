FROM python:3

EXPOSE 50051

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install grpcio grpcio-tools

CMD ["python", "grpc_server.py"]
