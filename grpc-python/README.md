# gRPC Python Example

Example of how to use protocol buffers and gRPC between different languages, including Python.

# Setup

## Protocol buffer compiler

> _protoc_ is already installed as part of _grpcio-tools_ package, so it is not necessary to install it like for other languages.

## Python

### Compiler Setup

Python is already a target language for protoc. No setup is required

> **TODO**: investigate the usage of C++ implementation for performance improvement.

### gRPC Setup

Install the grpcio-tools package (required for development only):

```
$ pip install grpcio-tools
```

### Project Setup

Install the following packages in your project:

```
$ pip install grpcio
```

# How to Compile

To generate client and server files from .proto files, execute the script _compile\_protos.bat_.

# How to Execute

Run the steps below to execute. The argument _--tls_ (to use a tls encrypted channel) is optional:
```
cd grpc-python/grpc_python
poetry run python server.py --tls
```
This will start a grpc server on _localhost:9090_.
