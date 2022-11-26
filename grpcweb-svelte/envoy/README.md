# Envoy Proxy Configuration for GRPC-WEB

This Envoy configuration:
- serves grpcweb requests to/from browser at port *8080*, and;
- proxies the requests to/from a local grpc server at port *9090* configured without TLS encryption.

## Envoy Configuration Files

Copy the desired .yaml file from _/config_ folder into _/mount_ as *envoy.yaml*.

Options:
- _envoy_basic.yaml_: basic configuration with no TLS encryption with the connection with the browser.
- _envoy_tls.yaml_: configuration with TLS encryption with the browser.

## TLS Certificates

The envoy configuration with TLS expects the following files inside /mount folder:

- _cert.pem_: server certificate
- _key.pem_: certificate private key

If you want to genereate a self signed certificate for development purposes, execute the script _generate_certificates.sh_ in the folder _tls-certificates_ and copy the files from there.
