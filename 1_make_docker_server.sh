cp ./test_python_vin/main.py ./docker/server
docker build -t mkud/test_python_vin:latest ./docker/server
