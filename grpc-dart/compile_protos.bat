@ECHO OFF

SET PROTOS=../protos
SET DART_OUT=./lib/autocode

protoc --dart_out=grpc:%DART_OUT% -Iprotos %PROTOS%/*.proto
