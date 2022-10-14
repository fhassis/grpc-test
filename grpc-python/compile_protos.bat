@ECHO OFF

SET PROTOS=../protocol_buffers/protos
SET PYTHON_OUT=./grpc_python/autocode

poetry run python -m grpc_tools.protoc -I %PROTOS% --python_out=%PYTHON_OUT% --grpc_python_out=%PYTHON_OUT% %PROTOS%/*.proto
