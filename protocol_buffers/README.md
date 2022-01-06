# ProtocolBuffer Example

Example of how to use protocol buffers and gRPC between different languages

# Setup

## Protocol buffer compiler

Download the protoc compiler from the link below and put it in PATH:

https://github.com/protocolbuffers/protobuf/releases

To check the version installed:

```
$ protoc --version
```

## Dart

### Compiler Setup

Install the protocol compiler plugin for Dart (protoc-gen-dart) using the following command:

```
$ dart pub global activate protoc_plugin
```

Update your PATH so that the protoc compiler can find the plugin. Example in linux:

```
$ export PATH="$PATH:$HOME/.pub-cache/bin"
```

### Project Setup

Install the following packages in your project:

```
$ dart pub add grpc protobuf
```

## Python

### Compiler Setup

Python is already a target language for protoc. No setup is required

> **TODO**: investigate the usage of C++ implementation for performance improvement.

### gRPC Setup

Install the grpcio-tools package:

```
$ pip install grpcio-tools
```

### Project Setup

Install the following packages in your project:

```
$ pip install grpcio
```
