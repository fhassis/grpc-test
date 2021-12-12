
# location of .proto files
PROTOS = ./protos

# location of Dart output files
DART_OUT = ./dart

greeter:
	protoc --dart_out=grpc:$(DART_OUT) -Iprotos $(PROTOS)/greeter.proto
