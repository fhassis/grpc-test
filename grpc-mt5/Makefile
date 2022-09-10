####################################
### PROTO FILES
####################################
PROTOS = ./proto-files


####################################
### PYTHON
####################################

PYTHON_OUT = ./grpc_autocode

grpc:
	poetry run python -m grpc_tools.protoc -I $(PROTOS) --python_out=$(PYTHON_OUT) --grpc_python_out=$(PYTHON_OUT) $(PROTOS)/*.proto
