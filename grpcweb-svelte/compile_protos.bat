SET PROTOS=../protos
SET JS_OUT=./src/autocode


@REM protoc -I=%PROTOS% %PROTOS%/greeter.proto --js_out=import_style=commonjs,binary:%JS_OUT% 

@REM @REM mode can be grpcwebtext (default) or grpcweb
@REM @REM protoc -I=%PROTOS% %PROTOS%/greeter.proto --grpc-web_out=import_style=typescript,mode=grpcwebtext:%JS_OUT%
@REM protoc -I=%PROTOS% %PROTOS%/greeter.proto --grpc-web_out=import_style=commonjs+dts,mode=grpcwebtext:%JS_OUT%



npx protoc --ts_out %JS_OUT% --proto_path %PROTOS% --ts_opt optimize_code_size %PROTOS%/greeter.proto
