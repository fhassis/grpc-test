
IMAGE=envoyproxy/envoy:v1.22.0
PORT=8080
CONFIG="$(pwd)"/mount

docker run -it -v $CONFIG:/etc/envoy -p $PORT:8080 $IMAGE
