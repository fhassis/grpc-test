@echo off

REM This script generates a self signed certificate with openssl for development purposes.

set TLS_OUT=.

openssl req -newkey rsa:2048 -nodes -keyout %TLS_OUT%/server.key -x509 -days 365 -out %TLS_OUT%/server.crt
