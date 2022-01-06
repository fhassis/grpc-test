####################################
### PROTO FILES
####################################
PROTOS = ../protocol_buffers/protos


####################################
### PYTHON
####################################

PYTHON_OUT = ./grpc_python/grpc_auto

grpc:
	poetry run python -m grpc_tools.protoc -I $(PROTOS) --python_out=$(PYTHON_OUT) --grpc_python_out=$(PYTHON_OUT) $(PROTOS)/greeter.proto
