@echo OFF

@REM SET PYTHONPATH=./grpc_python;./grpc_autocode;

cd grpc_python

poetry run python server.py
