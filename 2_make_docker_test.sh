cp ./test_python_vin/{main.py,test.py,test_data.py} ./docker/test
docker build -t mkud/test_python_vin_test:latest ./docker/test