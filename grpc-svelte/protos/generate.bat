SET PROTO_DIR=.
SET OUT_DIR=..\src\autocode
SET PROTO_FILES=helloworld.proto

MKDIR %OUT_DIR%

protoc -I=%PROTO_DIR% --js_out=import_style=commonjs,binary:%OUT_DIR% --grpc-web_out=import_style=typescript,mode=grpcwebtext:%OUT_DIR% %PROTO_FILES%
