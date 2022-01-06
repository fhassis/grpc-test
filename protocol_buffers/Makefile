####################################
### PROTO FILES
####################################
PROTOS = ./protos


####################################
### DART
####################################

DART_OUT = ./dart

dart:
	protoc --dart_out=grpc:$(DART_OUT) -Iprotos $(PROTOS)/greeter.proto


####################################
### PYTHON
####################################

PYTHON_OUT = ./python

python:
	echo > $(PYTHON_OUT)/__init__.py
	python -m grpc_tools.protoc -I $(PROTOS) --python_out=$(PYTHON_OUT) --grpc_python_out=$(PYTHON_OUT) $(PROTOS)/greeter.proto


####################################
### TLS CERTIFICATES
####################################

TLS_OUT = ./certificates

tls:
	openssl req -newkey rsa:2048 -nodes -keyout $(TLS_OUT)/server.key -x509 -days 365 -out $(TLS_OUT)/server.crt
