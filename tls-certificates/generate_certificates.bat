@echo off

REM This script generates a self signed certificate with openssl for development purposes.

set TLS_OUT=.

openssl req -x509 -nodes -newkey rsa:4096 -keyout %TLS_OUT%/key.pem -out %TLS_OUT%/cert.pem
