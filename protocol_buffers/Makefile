
# location of .proto files
PROTOS = ./protos

# location of Dart output files
DART_OUT = ./dart

# TLS certificate folder
TLS_OUT = ./certificates

greeter:
	protoc --dart_out=grpc:$(DART_OUT) -Iprotos $(PROTOS)/greeter.proto

tls:
	openssl req -newkey rsa:2048 -nodes -keyout $(TLS_OUT)/server.key -x509 -days 365 -out $(TLS_OUT)/server.crt
