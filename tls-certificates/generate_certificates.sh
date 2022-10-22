# Generates a self signed certificate for development purposes

TLS_OUT=.

openssl req -x509 -nodes -newkey rsa:4096 -keyout $TLS_OUT/key.pem -out $TLS_OUT/cert.pem
