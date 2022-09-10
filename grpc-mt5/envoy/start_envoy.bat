REM -it excecutes the command and leaves the terminal opened
REM -d executes the command as a daemon

docker run -it -v %CD%\mount:/etc/envoy -p 9090:9090 -p 9901:9901 envoyproxy/envoy:v1.17.0

pause